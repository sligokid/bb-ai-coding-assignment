# Do More Trees Mean More Money?

Determines whether residential properties on streets with tall trees sell for more, on average, than properties on streets with short trees in Dublin.

## Requirements

Python 3.10 or later.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

## Run

```bash
python main.py dublin-trees.json dublin-property.csv
```

## Test

```bash
pytest
```
