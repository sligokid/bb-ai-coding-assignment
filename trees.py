import csv
import json
from typing import Generator


def extract_street_names(node: dict) -> Generator[str, None, None]:
    """Recursively yield leaf keys (those whose values are integers)."""
    for key, value in node.items():
        if isinstance(value, int):
            yield key
        elif isinstance(value, dict):
            yield from extract_street_names(value)


def _detect_encoding(filepath: str) -> str:
    """Detect file encoding by trying common encodings in order."""
    with open(filepath, "rb") as f:
        raw = f.read()
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            raw.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Could not determine encoding for {filepath}")


def load_tree_categories(filepath: str) -> tuple[set[str], set[str]]:
    """Load trees JSON and return (short_streets, tall_streets)."""
    with open(filepath, encoding=_detect_encoding(filepath)) as f:
        data = json.load(f)
    short_streets = set(extract_street_names(data["short"]))
    tall_streets = set(extract_street_names(data["tall"]))
    return short_streets, tall_streets


def load_properties(filepath: str) -> list[dict]:
    """Read property CSV and return list of row dicts."""
    with open(filepath, encoding=_detect_encoding(filepath)) as f:
        return list(csv.DictReader(f))


def parse_price(price_str: str) -> float:
    """Parse a price string like '€79,500.00' into a float."""
    return float(price_str.replace("€", "").replace(",", ""))


def calculate_average_price(properties: list[dict], street_names: set[str]) -> float:
    """Return average sale price for properties on the given streets."""
    matching = [
        parse_price(row["Price"])
        for row in properties
        if row["Street Name"] in street_names
    ]
    if not matching:
        raise ValueError("No matching properties found")
    return sum(matching) / len(matching)
