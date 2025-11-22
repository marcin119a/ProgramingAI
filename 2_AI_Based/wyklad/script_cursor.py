import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import re

BASE_URL = "https://adresowo.pl"
PAGES = [f"https://adresowo.pl/mieszkania/warszawa/_l{i}" for i in range(1, 9)]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

results = []

def extract_text(tag):
    """Extract text from BeautifulSoup tag, return None if tag doesn't exist"""
    return tag.get_text(strip=True) if tag else None

def extract_number(text):
    """Extract number from text, removing spaces and non-numeric characters"""
    if not text:
        return None
    # Remove spaces and extract digits
    cleaned = re.sub(r'[^\d]', '', text)
    return cleaned if cleaned else None

for i, url in enumerate(PAGES):
    print(f"Scraping page {i+1}/8: {url}")
    
    # Add delay between requests to be respectful
    if i > 0:
        delay = random.uniform(2, 4)
        print(f"Waiting {delay:.1f} seconds...")
        time.sleep(delay)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        continue
    
    # Find all apartment listing sections
    items = soup.select("section.search-results__item")
    print(f"Found {len(items)} listings on this page")
    
    for item in items:
        # Extract URL
        link_tag = item.find("a", href=True)
        full_url = BASE_URL + link_tag["href"] if link_tag else None
        
        # Extract data-url if available (fallback)
        if not full_url:
            data_url = item.get("data-url")
            full_url = BASE_URL + data_url if data_url else None
        
        # locality (e.g., "Warszawa Targówek")
        locality_tag = item.select_one(".result-info__header strong")
        locality = extract_text(locality_tag)
        
        # street (e.g., "ul. Głębocka")
        street_tag = item.select_one(".result-info__address")
        street = extract_text(street_tag)
        
        # rooms (e.g., "3 pok.")
        rooms_tags = item.select(".result-info__basic-container__nodesc .result-info__basic")
        rooms = None
        if rooms_tags:
            rooms_text = extract_text(rooms_tags[0])
            if rooms_text:
                # Extract number from "3 pok." or similar
                rooms_match = re.search(r'(\d+)', rooms_text)
                rooms = rooms_match.group(1) if rooms_match else None
        
        # area (e.g., "68 m²")
        area = None
        if len(rooms_tags) > 1:
            area_text = extract_text(rooms_tags[1])
            if area_text:
                # Extract number from "68 m²" or similar
                area_match = re.search(r'(\d+)', area_text)
                area = area_match.group(1) if area_match else None
        
        # price_total_zl (e.g., "1 390 000")
        price_total_tag = item.select_one(".result-info__price--total span")
        price_total_text = extract_text(price_total_tag)
        price_total_zl = extract_number(price_total_text)
        
        # price_sqm_zl (e.g., "20 441")
        price_sqm_tag = item.select_one(".result-info__price--per-sqm span")
        price_sqm_text = extract_text(price_sqm_tag)
        price_sqm_zl = extract_number(price_sqm_text)
        
        # owner_type (check if "Bez pośredników" or similar)
        owner_tag = item.select_one(".result-info__basic--owner")
        owner_type = extract_text(owner_tag) if owner_tag else None
        # Normalize owner_type
        if owner_type:
            if "pośrednik" in owner_type.lower() or "bez pośredników" in owner_type.lower():
                owner_type = "Bez pośredników"
        else:
            owner_type = None
        
        # date_posted (e.g., "ponad tydzień temu")
        date_tag = item.select_one(".result-photo__date")
        date_posted = extract_text(date_tag)
        
        # photo_count (e.g., "14")
        photo_tag = item.select_one(".result-photo__photos span")
        photo_text = extract_text(photo_tag)
        photo_count = None
        if photo_text:
            # Extract number from text
            photo_match = re.search(r'(\d+)', photo_text)
            photo_count = photo_match.group(1) if photo_match else None
        
        # image_url
        image_tag = item.select_one(".result-photo__image")
        image_url = image_tag.get("src") if image_tag else None
        
        # Store the extracted data
        results.append({
            "locality": locality,
            "street": street,
            "rooms": rooms,
            "area": area,
            "price_total_zl": price_total_zl,
            "price_sqm_zl": price_sqm_zl,
            "owner_type": owner_type,
            "date_posted": date_posted,
            "photo_count": photo_count,
            "url": full_url,
            "image_url": image_url
        })

# Save to CSV
csv_file = "mieszkania_warszawa.csv"

if results:
    fieldnames = ["locality", "street", "rooms", "area", "price_total_zl", 
                  "price_sqm_zl", "owner_type", "date_posted", "photo_count", 
                  "url", "image_url"]
    
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\nSaved {len(results)} records to {csv_file}")
else:
    print("No data collected. Please check the website structure or network connection.")

