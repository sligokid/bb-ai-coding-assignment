import pytest

from trees import extract_street_names, load_tree_categories, parse_price


def test_extract_street_names():
    tree = {
        "zone_a": {
            "Elm Street": 5,
            "Oak Avenue": 12,
        },
        "zone_b": {
            "sub_zone": {
                "Pine Road": 8,
            },
            "Maple Drive": 3,
        },
    }
    result = set(extract_street_names(tree))
    assert result == {"Elm Street", "Oak Avenue", "Pine Road", "Maple Drive"}


def test_parse_price_valid():
    assert parse_price("€79,500.00") == 79500.0


def test_parse_price_invalid():
    with pytest.raises(ValueError):
        parse_price("not-a-price")
