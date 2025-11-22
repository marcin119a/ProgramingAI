import requests
from bs4 import BeautifulSoup
import csv
import time
import random

BASE_URL = "https://adresowo.pl"
PAGES = [f"https://adresowo.pl/mieszkania/warszawa/_l{i}" for i in range(1, 9)]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/123.0 Safari/537.36"
}

results = []

def extract_text(tag):
    return tag.get_text(strip=True) if tag else None

for i, url in enumerate(PAGES):
    print("Scraping:", url)
    
    # Opóźnienie między requestami (2-4 sekundy)
    if i > 0:
        delay = 1
        print(f"Oczekiwanie {delay:.1f} sekund przed następnym requestem...")
        time.sleep(delay)
    
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()  # Sprawdza status HTTP (rzuca wyjątek dla 4xx, 5xx)
        soup = BeautifulSoup(r.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania {url}: {e}")
        continue

    items = soup.select("section.search-results__item")

    for item in items:
        data_id = item.get("data-id")
        link_tag = item.find("a", href=True)
        full_url = BASE_URL + link_tag["href"] if link_tag else None

        # locality
        locality = extract_text(item.select_one(".result-info__header strong"))

        # street
        street = extract_text(item.select_one(".result-info__address"))

        # rooms
        rooms_raw = extract_text(item.select_one(".result-info__basic-container__nodesc .result-info__basic:nth-of-type(1)"))
        rooms = rooms_raw.replace(" pok.", "") if rooms_raw else None

        # area
        area_raw = extract_text(item.select_one(".result-info__basic-container__nodesc .result-info__basic:nth-of-type(2)"))
        area = area_raw.replace(" m²", "") if area_raw else None

        # owner_type
        owner_type = "owner" if item.select_one(".result-info__basic--owner") else "unknown"

        # price total
        price_total_tag = item.select_one(".result-info__price--total span")
        price_total = extract_text(price_total_tag)
        if price_total:
            price_total = price_total.replace(" ", "").replace("zł", "")

        # price per sqm
        price_sqm_tag = item.select_one(".result-info__price--per-sqm span")
        price_sqm = extract_text(price_sqm_tag)
        if price_sqm:
            price_sqm = price_sqm.replace(" ", "").replace("zł/m²", "").replace("zł", "")

        # date posted
        date_posted = extract_text(item.select_one(".result-photo__date"))

        # photo count
        photo_raw = extract_text(item.select_one(".result-photo__photos span"))
        photo_count = None
        if photo_raw:
            try:
                photo_count = int(photo_raw.split()[-1])
            except:
                pass

        # image_url
        image_tag = item.select_one(".result-photo__image")
        image_url = image_tag["src"] if image_tag else None

        results.append({
            "locality": locality,
            "street": street,
            "rooms": rooms,
            "area": area,
            "price_total_zl": price_total,
            "price_sqm_zl": price_sqm,
            "owner_type": owner_type,
            "date_posted": date_posted,
            "photo_count": photo_count,
            "url": full_url,
            "image_url": image_url
        })


# ============================
# SAVE RESULTS TO CSV
# ============================

csv_file = "mieszkania_warszawa_gpt.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"Zapisano {len(results)} rekordów do pliku: {csv_file}")