# FastAPI Project

## Instalacja

1. Utwórz środowisko wirtualne:
   - Linux/Mac:
   ```bash
   python3 -m venv venv
   ```
   - Windows:
   ```bash
   python -m venv venv
   ```

2. Aktywuj środowisko wirtualne:
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```
   - Windows:
   ```bash
   venv\Scripts\activate
   ```

3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

## Uruchomienie

```bash
uvicorn main:app --reload
```

Aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000`

## Dokumentacja

Dostępna pod adresem: `http://127.0.0.1:8000/docs`

