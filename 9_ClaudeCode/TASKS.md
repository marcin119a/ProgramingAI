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
