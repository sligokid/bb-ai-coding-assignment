import pytest

from trees import calculate_average_price, extract_street_names, load_tree_categories, parse_price


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


def test_calculate_average_price():
    properties = [
        {"Street Name": "Elm Street", "Price": "€100,000.00"},
        {"Street Name": "Elm Street", "Price": "€200,000.00"},
        {"Street Name": "Oak Avenue", "Price": "€300,000.00"},
    ]
    result = calculate_average_price(properties, {"Elm Street"})
    assert result == 150000.0


def test_calculate_average_price_no_matches():
    properties = [
        {"Street Name": "Elm Street", "Price": "€100,000.00"},
    ]
    with pytest.raises(ValueError, match="No matching properties found"):
        calculate_average_price(properties, {"Unknown Street"})
