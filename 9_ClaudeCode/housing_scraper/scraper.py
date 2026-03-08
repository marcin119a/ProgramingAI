import csv
import time
from pathlib import Path

import requests

from parser import parse_listings

BASE_URL = "https://adresowo.pl"
PAGES_URL = "https://adresowo.pl/mieszkania/lodz/_l{page}"
FIRST_PAGE_URL = "https://adresowo.pl/mieszkania/lodz/_l1"
OUTPUT_CSV = Path(__file__).parent / "adresowo_lodz.csv"
FIELDNAMES = ["id", "url", "locality", "rooms", "area_m2", "price_total_zl", "price_per_m2_zl"]
PAGES = range(1, 9)  # _l1 to _l8
DELAY_SECONDS = 1.5


def fetch_html(url: str, timeout: int = 20) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8",
    }
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text


def save_csv(listings: list[dict], path: Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(listings)
    print(f"Saved {len(listings)} listings to {path}")


def scrape_all_pages() -> list[dict]:
    all_listings: list[dict] = []
    seen_ids: set[str] = set()

    for page in PAGES:
        url = PAGES_URL.format(page=page)
        print(f"Fetching page {page}/8: {url}")
        try:
            html = fetch_html(url)
        except requests.HTTPError as e:
            print(f"  HTTP error {e.response.status_code}, stopping.")
            break
        except requests.RequestException as e:
            print(f"  Request failed: {e}, stopping.")
            break

        listings = parse_listings(html)
        new = [l for l in listings if l["id"] not in seen_ids]
        seen_ids.update(l["id"] for l in new)
        all_listings.extend(new)
        print(f"  Parsed {len(listings)} listings, {len(new)} new (total: {len(all_listings)})")

        if page < PAGES[-1]:
            time.sleep(DELAY_SECONDS)

    return all_listings


def main() -> None:
    listings = scrape_all_pages()
    if listings:
        save_csv(listings, OUTPUT_CSV)
    else:
        print("No listings found.")


if __name__ == "__main__":
    main()
