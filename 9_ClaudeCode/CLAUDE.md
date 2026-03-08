# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Housing scraper for **adresowo.pl** — scrapes apartment listings for Łódź, parses HTML, and exports to CSV/XLSX. Written in Python, uses BeautifulSoup for parsing.

## Commands

```bash
# Run the scraper
cd housing_scraper && python scraper.py

# Run all tests
cd housing_scraper && pytest tests/

# Run a single test
cd housing_scraper && pytest tests/test_parser.py -k test_listing_count
```

## Dependencies

Install with: `pip install requests beautifulsoup4 openpyxl pytest`

## Architecture

The project lives in `housing_scraper/` with three main modules:

- **`parser.py`** — `parse_listings(html)` extracts listing dicts from HTML using BeautifulSoup. Each listing has: `id`, `url`, `locality`, `rooms`, `area_m2`, `price_total_zl`, `price_per_m2_zl`. All values are strings.
- **`scraper.py`** — `scrape_all_pages()` fetches pages `_l1` through `_l8`, deduplicates by offer ID, and calls export. Entry point is `main()`.
- **`export.py`** — `save_csv()` and `save_xlsx()` write listings to file. Numeric fields (`rooms`, `area_m2`, `price_total_zl`, `price_per_m2_zl`) are converted to int in XLSX output.

## Conventions

- Follow PEP 8
- Tests use pytest with fixtures in `tests/fixtures/` (e.g., `sample_page.html`)
- Test files use `tmp_path` fixture for file output tests
- Parser tests import `parser.py` directly (tests run from `housing_scraper/` directory)
- All CSV output is UTF-8 encoded

## Task Backlog

`TASKS.md` contains pending work items (TASK-03 through TASK-06): extended CSV options, `--format` CLI argument, export tests, and documentation updates.
