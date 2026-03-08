# TASKS — Rozszerzenie systemu raportowania

## Cel

Rozbudowanie modułu eksportu danych o obsługę formatów **XLSX** i **CSV** (z rozszerzonym konfigurowaniem), wydzielenie logiki eksportu do osobnego modułu oraz pokrycie zmian testami.

---

## TASK-01 — Wydzielenie modułu `export.py`

**Opis:**
Przenieś funkcję `save_csv` z `scraper.py` do nowego modułu `housing_scraper/export.py`. Scraper powinien importować funkcje eksportu z tego modułu.

**Pliki do zmiany:**
- `housing_scraper/scraper.py` — usuń `save_csv`, dodaj import z `export`
- `housing_scraper/export.py` — nowy plik

**Sygnatura funkcji:**
```python
def save_csv(listings: list[dict], path: Path, fieldnames: list[str] | None = None) -> None:
    ...
```

**Kryteria akceptacji:**
- [x] Plik `export.py` istnieje
- [x] `scraper.py` nie zawiera już logiki zapisu do pliku
- [x] Dotychczasowe działanie scrapera nie ulega zmianie

---

## TASK-02 — Eksport do XLSX

**Opis:**
Dodaj do `export.py` funkcję `save_xlsx`, która zapisuje dane do pliku Excel (`.xlsx`) z użyciem biblioteki `openpyxl`.

**Wymagania:**
- Pierwszy wiersz arkusza to nagłówki (pogrubione)
- Kolumny liczbowe (`rooms`, `area_m2`, `price_total_zl`, `price_per_m2_zl`) zapisywane jako liczby całkowite
- Szerokość kolumn dopasowana automatycznie do zawartości
- Arkusz nazwany `Listings`

**Sygnatura funkcji:**
```python
def save_xlsx(listings: list[dict], path: Path, fieldnames: list[str] | None = None) -> None:
    ...
```

**Nowa zależność:**
```
openpyxl
```

**Kryteria akceptacji:**
- [x] Plik `.xlsx` otwiera się poprawnie w Excelu / LibreOffice
- [x] Nagłówki są pogrubione
- [x] Kolumny numeryczne mają typ liczbowy (nie tekstowy)
- [x] Kolumny mają rozsądną szerokość

---

## TASK-03 — Rozszerzony eksport CSV

**Opis:**
Rozszerz funkcję `save_csv` o opcje konfiguracyjne: wybór separatora, kodowania i pola do pominięcia.

**Sygnatura funkcji:**
```python
def save_csv(
    listings: list[dict],
    path: Path,
    fieldnames: list[str] | None = None,
    separator: str = ",",
    encoding: str = "utf-8",
    exclude_fields: list[str] | None = None,
) -> None:
    ...
```

**Kryteria akceptacji:**
- [ ] Domyślne zachowanie (separator `,`, encoding `utf-8`) zgodne z poprzednią wersją
- [ ] Możliwość eksportu z separatorem `;` (np. dla Excela w polskich ustawieniach regionalnych)
- [ ] Możliwość pominięcia wybranych kolumn (np. `url`)

---

## TASK-04 — Integracja eksportu w `scraper.py`

**Opis:**
Zaktualizuj funkcję `main()` w `scraper.py` tak, aby obsługiwała argument `--format` pozwalający wybrać format wyjściowy.

**Obsługiwane formaty:**
- `csv` (domyślny)
- `xlsx`
- `all` — zapisuje oba formaty jednocześnie

**Przykład użycia:**
```bash
python scraper.py --format xlsx
python scraper.py --format all
```

**Kryteria akceptacji:**
- [ ] Argument `--format` działa poprawnie dla wszystkich trzech opcji
- [ ] Pliki wyjściowe: `adresowo_lodz.csv` i/lub `adresowo_lodz.xlsx`
- [ ] Brak argumentu działa jak `--format csv`

---

## TASK-05 — Testy jednostkowe eksportu

**Opis:**
Napisz testy dla modułu `export.py` w pliku `housing_scraper/tests/test_export.py`.

**Testy do napisania:**

| test | opis |
|------|------|
| `test_save_csv_creates_file` | plik CSV zostaje utworzony |
| `test_save_csv_headers` | nagłówki CSV są poprawne |
| `test_save_csv_row_count` | liczba wierszy odpowiada liczbie ogłoszeń |
| `test_save_csv_separator` | separator `;` działa poprawnie |
| `test_save_csv_exclude_fields` | wykluczone pola nie pojawiają się w pliku |
| `test_save_xlsx_creates_file` | plik XLSX zostaje utworzony |
| `test_save_xlsx_headers` | nagłówki w XLSX są poprawne |
| `test_save_xlsx_numeric_columns` | kolumny numeryczne mają typ `int` |

**Kryteria akceptacji:**
- [ ] Wszystkie 8 testów przechodzi (`pytest tests/`)
- [ ] Testy używają `tmp_path` fixture (nie zapisują do katalogu projektu)

---

## TASK-06 — Aktualizacja dokumentacji

**Opis:**
Zaktualizuj `README.md` i `SKILLS.md` po wprowadzeniu zmian.

**Zmiany w README.md:**
- Dodaj sekcję "Formaty eksportu" opisującą CSV i XLSX
- Dodaj `openpyxl` do listy wymagań
- Zaktualizuj przykłady uruchomienia (`--format`)

**Zmiany w SKILLS.md:**
- Dodaj `openpyxl` do listy bibliotek
- Opisz nowe możliwości eksportu

**Kryteria akceptacji:**
- [ ] README zawiera aktualną listę zależności
- [ ] README zawiera przykłady użycia `--format`

---

## Kolejność realizacji

```
TASK-01 → TASK-02 → TASK-03 → TASK-04 → TASK-05 → TASK-06
```

TASK-02 i TASK-03 można realizować równolegle po ukończeniu TASK-01.

---

## TASK-07 — Statystyki rynku mieszkań (Story 1)

**Opis:**
Nowy moduł `housing_app/processing/stats.py` oblicza podstawowe statystyki rynku na podstawie listy ogłoszeń.

**Zakres:**
- średnia cena za m²
- mediana ceny za m²
- statystyki per lokalizacja (liczba ofert, średnia i mediana ceny za m²)
- łączna liczba ofert

**Nowy plik:** `housing_app/processing/stats.py`

**Sygnatura funkcji:**
```python
def compute_stats(listings: list[dict]) -> dict:
    """
    Zwraca słownik z polami:
    - count: int
    - avg_price_per_m2: float | None
    - median_price_per_m2: float | None
    - by_locality: dict[str, dict]  # każdy wpis: count, avg, median
    """
    ...
```

**Wymagania:**
- Ignoruje ogłoszenia z brakującą lub pustą wartością `price_per_m2_zl`
- Wartości `price_per_m2_zl` traktuje jako liczby całkowite (string → int)
- Nie wymaga zewnętrznych bibliotek (tylko `statistics` ze stdlib)
- Re-eksport przez `housing_app/processing/__init__.py`

**Testy:** `housing_app/tests/test_stats.py`

| test | opis |
|------|------|
| `test_compute_stats_count` | poprawna liczba ofert |
| `test_compute_stats_avg` | poprawna średnia ceny za m² |
| `test_compute_stats_median` | poprawna mediana ceny za m² |
| `test_compute_stats_ignores_missing` | ogłoszenia bez ceny za m² są pomijane |
| `test_compute_stats_by_locality` | statystyki per lokalizacja są poprawne |
| `test_compute_stats_empty` | pusta lista zwraca `count=0`, `avg=None`, `median=None` |

**Kryteria akceptacji:**
- [ ] `compute_stats` zwraca poprawne wyniki dla typowych danych
- [ ] Brakujące / puste wartości `price_per_m2_zl` są ignorowane (nie powodują błędu)
- [ ] Wszystkie 6 testów przechodzi (`pytest housing_app/tests/test_stats.py`)
- [ ] Testy używają `tmp_path` lub danych in-memory (bez zapisu do pliku)
