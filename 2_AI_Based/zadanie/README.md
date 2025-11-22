### Zadanie 1

Pobrać dane o ogłoszeniach mieszkań w Łodzi z portalu adresowo.pl, wyczyścić je i zapisać do pliku CSV, aby móc później analizować ceny i cechy mieszkań.

---

### 🛠️ Co powinien robić kod?

1. **Import bibliotek**

   * `requests` – pobieranie stron www,
   * `BeautifulSoup` – parsowanie HTML i wyciąganie danych,
   * `csv` – zapis wyników,
   * `time` – opóźnienie między zapytaniami (żeby nie przeciążać serwera).

2. **Definicja parametrów scrapera**

   * `BASE_URL` – link do wyszukiwania mieszkań w Łodzi (z paginacją),
   * `HEADERS` – nagłówek z „User-Agent”, żeby udawać normalną przeglądarkę.

3. **Pętla po stronach**

   * Iteruje po 8 stronach wyników (od 1 do 8),
   * Pobiera HTML strony,
   * Szuka sekcji `section.search-results__item` (każde ogłoszenie).

4. **Ekstrakcja danych z ogłoszeń**
   Dla każdego ogłoszenia zbierane są informacje:

   * `id`, `url` – identyfikator i link do ogłoszenia,
   * `date_posted` – data dodania ogłoszenia,
   * `photos` – liczba zdjęć,
   * `locality`, `street` – dzielnica i ulica,
   * `property_type` – typ nieruchomości,
   * `rooms` – liczba pokoi,
   * `area_m2` – powierzchnia mieszkania,
   * `owner_direct` – czy ogłoszenie jest bezpośrednio od właściciela,
   * `price_total_zl` – cena całkowita,
   * `price_per_m2_zl` – cena za metr kwadratowy.

5. **Dodanie danych do listy**

   * Dane zapisywane są jako słownik w liście `results`.

6. **Opóźnienie między żądaniami**

   * `time.sleep(1)` → każda kolejna strona pobierana jest po 1 sekundzie (tzw. polite scraping).

7. **Zapis do CSV**

   * Jeśli zebrano dane, program tworzy plik `adresowo_lodz.csv` i zapisuje wszystkie rekordy.

---

### Wynik

Na końcu mamy plik **`adresowo_lodz.csv`** zawierający zestaw danych o mieszkaniach w Łodzi – gotowy do dalszej analizy w Pandas (np. sprawdzanie median cen, rozkład metraży, analiza dzielnic).
