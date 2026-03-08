# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Housing scraper for **adresowo.pl** — scrapes apartment listings for Łódź, parses HTML, and exports to CSV/XLSX. Written in Python, uses BeautifulSoup for parsing.

## Commands

```bash
# Install package in editable mode
pip install -e .

# Run the scraper
python -m housing_app

# Run all tests
pytest housing_app/tests/

# Run a single test
pytest housing_app/tests/test_parser.py -k test_listing_count
```

## Dependencies

Managed via `pyproject.toml`. Install with: `pip install -e ".[dev]"`

## Architecture

The project is structured as the `housing_app` package with domain-based subpackages:

```
housing_app/
├── __init__.py
├── __main__.py              # scrape_all_pages() + main() entry point
├── scraper/
│   ├── __init__.py          # re-exports fetch_html, parse_listings
│   ├── downloader.py        # fetch_html() + URL constants
│   └── parser.py            # parse_listings() — HTML parsing with BeautifulSoup
├── processing/
│   ├── __init__.py          # re-exports filter_listings
│   ├── filters.py           # filter_listings() — filter by price, area, rooms, locality
│   └── ranking.py           # rank_listings() placeholder
├── export/
│   ├── __init__.py          # DEFAULT_FIELDNAMES, NUMERIC_FIELDS constants + re-exports
│   ├── csv_export.py        # save_csv()
│   └── xlsx_export.py       # save_xlsx()
└── tests/
    ├── __init__.py
    ├── test_parser.py
    ├── test_filter.py
    └── fixtures/
        └── sample_page.html
```

Each listing dict has: `id`, `url`, `locality`, `rooms`, `area_m2`, `price_total_zl`, `price_per_m2_zl`. All values are strings.

## Conventions

- Follow PEP 8
- Use absolute imports (`from housing_app.scraper.parser import parse_listings`)
- Tests use pytest with fixtures in `tests/fixtures/`
- Test files use `tmp_path` fixture for file output tests
- All CSV output is UTF-8 encoded

## Task Backlog

`TASKS.md` contains pending work items (TASK-03 through TASK-06): extended CSV options, `--format` CLI argument, export tests, and documentation updates.
