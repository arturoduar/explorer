# explorer

Explore small data sets.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
explorer
# or
python -m explorer.main
```

## Test

```bash
pytest
```

## Layout

```
explorer/
├── pyproject.toml
├── README.md
├── src/explorer/
│   ├── __init__.py
│   └── main.py
└── tests/
    └── test_main.py
```
