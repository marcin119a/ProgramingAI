
# Zadanie warsztatowe

# Ewolucyjna architektura z Claude Code

## Cel zadania

Celem jest **przekształcenie monolitycznej aplikacji w bardziej modularny system** z pomocą Claude Code.

Podczas zadania uczestnicy:

* przeanalizują istniejący kod
* zaproponują poprawę architektury
* podzielą kod na moduły
* dodadzą testy
* utworzą plik **SKILLS.md**, który pomoże agentowi AI pracować z projektem

---

# Stan początkowy aplikacji

Projekt analizuje ogłoszenia mieszkań.

Struktura repozytorium:

```
housing_app/
│
├── app.py
├── parser.py
├── utils.py
├── sample_page.html
└── adresowo_lodz.csv
```

Problemy:

* duże pliki
* brak modularności
* brak testów
* brak dokumentacji dla AI

---
# Zadanie 0

# Dodanie pliku SKILLS.md

Dodaj do repozytorium plik:

```
SKILLS.md
```

Plik powinien zawierać:

* strukturę projektu
* zasady architektury
* sposób uruchamiania testów
* typowe zadania agenta

Przykład:

```markdown
# AI Skills for this Repository

## Architecture

The project follows modular architecture.

Modules:

scraper
processing
export
tests

Avoid large monolithic files.

# Zadanie 1

# Plan refaktoryzacji

Użyj Claude do zaplanowania zmian.

Komenda:

```
/plan improve modular architecture
```

Claude powinien zaproponować podział aplikacji.

Docelowa struktura może wyglądać np.:

```
housing_app/

scraper/
    downloader.py
    parser.py

processing/
    filters.py
    ranking.py

export/
    csv_export.py

tests/
```

---

# Zadanie 2

# Refaktoryzacja aplikacji

Użyj Claude Code do podziału dużych plików.

```
Split this module into smaller components following the single responsibility principle.
```

Cel:

* wydzielić logikę parsowania
* wydzielić logikę przetwarzania danych
* wydzielić eksport danych



## Testing

Testing framework: pytest

Run tests:

pytest tests/

## Refactoring

Follow the single responsibility principle.

Large files should be split into smaller modules.
```

---