# Zadanie warsztatowe

# Automatyzacja testów z GitHub Actions

## Cel zadania

Twoim zadaniem jest rozszerzenie aplikacji o **automatyczne testowanie kodu przy użyciu GitHub Actions**.

Pipeline CI powinien:

* uruchamiać testy jednostkowe
* sprawdzać poprawność instalacji projektu
* uruchamiać się automatycznie przy każdym pushu do repozytorium

---

# Kontekst projektu

Projekt analizuje ogłoszenia mieszkań.

Struktura repozytorium po refaktoryzacji:

```text
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
    test_parser.py
    test_filters.py

SKILLS.md
requirements.txt
```

Projekt wykorzystuje:

* Python
* pytest
* BeautifulSoup

---

# Zadanie 1

# Analiza projektu przy użyciu Claude Code

Najpierw poproś Claude Code o analizę repozytorium.

Komenda:

```
/review
```

lub

```
Analyze this repository and identify how tests should be executed.
```

Claude powinien wskazać:

* że testy znajdują się w katalogu `tests`
* że używany jest framework **pytest**

---

# Zadanie 2

# Zaplanowanie pipeline CI

Poproś Claude o zaplanowanie pipeline CI.

Komenda:

```
/plan create GitHub Actions workflow for running tests
```

Claude powinien zaproponować kroki:

1. uruchomienie środowiska Python
2. instalacja zależności
3. uruchomienie pytest

---

# Zadanie 3

# Utworzenie workflow GitHub Actions

Dodaj plik:

```text
.github/workflows/tests.yml
```

---

# Zadanie 4

# Dodanie informacji do SKILLS.md

Rozszerz plik **SKILLS.md**, aby agent AI wiedział jak działa CI.

Dodaj sekcję:

```markdown
## Continuous Integration

This project uses GitHub Actions for automated testing.

Workflow file:

.github/workflows/tests.yml

Pipeline steps:

1. install dependencies
2. run pytest
3. verify tests pass
```

Dzięki temu Claude Code będzie wiedział:

* jak działa pipeline
* jak uruchamiać testy

---

# Zadanie 5

# Weryfikacja pipeline

Po dodaniu workflow:

1. wykonaj **commit**
2. wypchnij zmiany do repozytorium
3. sprawdź zakładkę **Actions** w GitHub

Pipeline powinien:

* uruchomić się automatycznie
* wykonać testy

---

# Zadanie 6

# Ulepszenie pipeline przy użyciu Claude Code

Poproś Claude o ulepszenie pipeline.

Komenda:

```
Analyze this GitHub Actions workflow and suggest improvements.
```

Claude może zaproponować:

* cache dependencies
* sprawdzanie stylu kodu
* test coverage

---

