# Housing Scraper — adresowo.pl

Scraper ogłoszeń mieszkań z portalu **adresowo.pl** dla miasta Łódź. Projekt powstał w ramach ćwiczeń z Claude Code.

## Opis

Program pobiera dane o ogłoszeniach mieszkań, parsuje je z HTML i zapisuje do pliku CSV. Dane obejmują: cenę, powierzchnię, liczbę pokoi, lokalizację oraz wyliczoną cenę za m².

## Struktura projektu

```
housing_scraper/
├── scraper.py              # pobieranie stron i zapis do CSV
├── parser.py               # parsowanie HTML (BeautifulSoup)
├── inspect_html.py         # narzędzie pomocnicze do inspekcji HTML
├── adresowo_lodz.csv       # wynikowy plik CSV
└── tests/
    ├── test_parser.py      # testy jednostkowe parsera
    └── fixtures/
        └── sample_page.html  # przykładowy HTML do testów
```

## Wymagania

```
requests
beautifulsoup4
pytest
```

Instalacja zależności:

```bash
pip install requests beautifulsoup4 pytest
```

## Uruchomienie scrapera

```bash
cd housing_scraper
python scraper.py
```

Scraper pobiera strony `_l1` do `_l8` z adresowo.pl, deduplikuje ogłoszenia i zapisuje wyniki do `adresowo_lodz.csv`.

## Format danych wyjściowych

| pole              | opis                     |
|-------------------|--------------------------|
| `id`              | identyfikator ogłoszenia |
| `url`             | link do ogłoszenia       |
| `locality`        | dzielnica                |
| `rooms`           | liczba pokoi             |
| `area_m2`         | powierzchnia w m²        |
| `price_total_zl`  | cena całkowita w PLN     |
| `price_per_m2_zl` | cena za m² (wyliczona)   |

Przykład:

```
id,url,locality,rooms,area_m2,price_total_zl,price_per_m2_zl
3920246,https://adresowo.pl/...,Łódź Bałuty,3,44,383000,8705
```

## Testy

```bash
cd housing_scraper
pytest tests/
```

Testy sprawdzają:
- liczbę sparsowanych ogłoszeń
- obecność wszystkich wymaganych pól
- poprawność danych (cena, powierzchnia, pokoje, cena za m²)
