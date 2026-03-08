# Zadanie: Web scraping ogłoszeń mieszkań z użyciem Claude Code

## Cel zadania

Celem zadania jest stworzenie programu w Pythonie, który:

* parsuje dane o ogłoszeniach mieszkań w Łodzi
* czyści dane
* zapisuje je do pliku CSV
* posiada **testy jednostkowe**

W zadaniu wykorzystujemy **Claude Code**, który pomoże wygenerować kod i testy.

---

# Kontekst projektu

Chcemy pobrać dane o ogłoszeniach mieszkań w Łodzi z portalu **adresowo.pl**, aby później analizować:

* ceny mieszkań
* powierzchnię
* liczbę pokoi
* lokalizację
* cenę za metr kwadratowy

W zadaniu **będziemy scrapować prawdziwą strone**, i użyjemy **przykładowego HTML**, który pokazuje strukturę ogłoszeń.

---

# Struktura projektu

Projekt powinien mieć następującą strukturę:

```
housing_scraper/
│
├── scraper.py
├── parser.py
├── sample_page.html
├── test_parser.py
└── adresowo_lodz.csv
```

---

# Krok 1 — wygeneruj scraper z pomocą Claude Code

Użyj Claude Code i poproś model o wygenerowanie kodu, który:

* wczyta HTML strony z wykorzystaniem requests
* sparsuje ogłoszenia
* zapisze dane do CSV

Przykładowe polecenie w Claude Code:

```
Create a Python scraper that parses apartment listings
from an HTML page using requests and saves them to CSV.
Use BeautifulSoup and create clean structured output. In file example.html is an example section.  
```

---

# Krok 2 — kod HTML ze strony adresowo.pl

Zapisz przykładowy plik jako **sample_page.html**.


---

# Krok 3 — wymagane pola danych

Parser powinien wyciągać następujące dane:

| pole            | opis                     |
| --------------- | ------------------------ |
| id              | identyfikator ogłoszenia |
| url             | link do ogłoszenia       |
| locality        | dzielnica                |
| rooms           | liczba pokoi             |
| area_m2         | powierzchnia             |
| price_total_zl  | cena całkowita           |
| price_per_m2_zl | cena za m²               |

---

# Krok 4 — zapis danych

Program powinien zapisać dane do pliku:

```
adresowo_lodz.csv
```

Przykładowy wynik:

```
id,locality,rooms,area_m2,price_total_zl,price_per_m2_zl
12345,Łódź Bałuty,3,50,450000,9000
12346,Łódź Widzew,2,52,520000,10000
```

---

# Krok 5 — dodaj testy jednostkowe

Z pomocą Claude Code wygeneruj **proste testy jednostkowe**.

Użyj biblioteki:

```
pytest
```

Przykładowe polecenie dla Claude Code:

```
Generate unit tests for the HTML parser using pytest.
The tests should verify that:

- the parser extracts correct number of listings
- the price is parsed correctly
- the area is parsed correctly
```

---

# Przykładowe testy


---

# Oczekiwany rezultat

Na końcu projektu powinieneś mieć:

✔ działający parser HTML
✔ zapis danych do CSV
✔ minimum **3 testy jednostkowe**
✔ kod wygenerowany i poprawiony przy pomocy **Claude Code**

---

# Zadanie dodatkowe (dla chętnych)

Poproś Claude Code o:

* dodanie **walidacji danych**
* obsługę brakujących wartości
* dodanie **testów edge case**

np.

```
Add for this parser validation to data to make it more robust and handle missing fields.
```

---