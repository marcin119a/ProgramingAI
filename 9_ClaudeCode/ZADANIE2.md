# Zadanie: Rozbudowa aplikacji z użyciem Claude Code i SKILLS.md

## Cel zadania

Twoim zadaniem jest **rozbudowanie istniejącej aplikacji analizującej ogłoszenia mieszkań** oraz przygotowanie repozytorium tak, aby **agent AI (Claude Code)** mógł efektywnie pracować z projektem.

W zadaniu:

* rozszerzysz funkcjonalność aplikacji
* napiszesz testy jednostkowe
* przygotujesz plik **`SKILLS.md`**, który opisuje możliwości AI w repozytorium

---

# Stan początkowy aplikacji

Aplikacja:

* parsuje dane z HTML
* zapisuje wyniki do CSV

Struktura projektu:

```
housing_scraper/
│
├── scraper.py
├── parser.py
├── sample_page.html
├── export.py
├── tests/
└── adresowo_lodz.csv
```

Parser zwraca listę słowników:

```
[
  {
    "id": "12345",
    "locality": "Łódź Bałuty",
    "rooms": 3,
    "area_m2": 50,
    "price_total_zl": 450000
  }
]
```

# Zadanie 0 — Dodanie pliku SKILLS.md

Dodaj do repozytorium plik:

```
SKILLS.md
```

Plik powinien opisywać:

* jakie zadania może wykonywać Claude Code
* jakie biblioteki są używane
* jak uruchamiać testy
* jak wygląda struktura projektu

Przykład:

```markdown
# AI Skills for this Repository

## Code Generation
Generate Python code following PEP8 guidelines.

## Testing
Use pytest to create and run unit tests.

Run tests with:

pytest tests/

## Data Processing
The project processes housing listings parsed from HTML.

Libraries used:
- beautifulsoup4
- requests
- csv

## Refactoring
The agent can refactor modules to improve readability.
```


---

# Zadanie 1 — Dodanie filtrowania danych

Dodaj funkcję filtrowania ogłoszeń.

Funkcja powinna umożliwiać:

* filtrowanie po **liczbie pokoi**
* filtrowanie po **maksymalnej cenie**
* filtrowanie po **dzielnicy**

Przykład funkcji:

```python
filter_listings(data, min_rooms=None, max_price=None, locality=None)
```

---

# Zadanie 2 — Obliczanie ceny za metr kwadratowy

Dodaj funkcję obliczającą:

```
price_per_m2
```

dla każdego ogłoszenia.

Przykład:

```
price_total_zl = 450000
area_m2 = 50

price_per_m2 = 9000
```

Wartość powinna zostać dodana do struktury danych.

---

# Zadanie 3 — Ranking mieszkań

Dodaj funkcję zwracającą **najlepsze oferty mieszkań**.

Funkcja powinna:

* sortować ogłoszenia według ceny za m²
* zwracać **top 5 najtańszych mieszkań**

Przykład:

```python
get_best_deals(data, n=5)
```

---

# Zadanie 4 — Testy jednostkowe

Napisz testy jednostkowe przy użyciu **pytest**.

Testy powinny sprawdzać:

* filtrowanie danych
* poprawność obliczania ceny za m²
* poprawność rankingu

Przykład testu:

```python
def test_price_per_m2():

    listing = {
        "price_total_zl": 450000,
        "area_m2": 50
    }

    result = compute_price_per_m2(listing)

    assert result == 9000
```

---

# Zadanie 5 — Wykorzystanie Claude Code

Podczas pracy nad zadaniem użyj Claude Code do:

* analizy struktury projektu
* generowania nowych funkcji
* tworzenia testów jednostkowych
* refaktoryzacji kodu

Przykładowe polecenia:

```
Analyze this repository and suggest where to implement filtering functionality.
```

```
Generate pytest tests for the filtering function.
```

```
Refactor this module to make it more modular.
```

---

# Zadanie dodatkowe (dla chętnych)

Rozszerz projekt o:

* zapis danych do **JSON**

