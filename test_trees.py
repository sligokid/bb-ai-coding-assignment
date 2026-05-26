import tempfile
import os

import pytest

from trees import _detect_encoding, calculate_average_price, extract_street_names, load_tree_categories, parse_price


def _write_tmp(content: bytes) -> str:
    fd, path = tempfile.mkstemp()
    os.write(fd, content)
    os.close(fd)
    return path


def test_detect_encoding_utf8():
    path = _write_tmp("hello".encode("utf-8"))
    try:
        assert _detect_encoding(path) == "utf-8-sig"
    finally:
        os.unlink(path)


def test_detect_encoding_utf8_sig():
    path = _write_tmp("\ufeffhello".encode("utf-8-sig"))
    try:
        assert _detect_encoding(path) == "utf-8-sig"
    finally:
        os.unlink(path)


def test_detect_encoding_cp1252():
    # b'\x80' is valid cp1252 (€) but not valid utf-8 or utf-8-sig
    path = _write_tmp(b"caf\x80")
    try:
        assert _detect_encoding(path) == "cp1252"
    finally:
        os.unlink(path)


def test_detect_encoding_unknown_raises():
    # b'\x81' is invalid in cp1252
    path = _write_tmp(b"\x81\x8d\x8f\x90\x9d")
    try:
        with pytest.raises(ValueError, match="Could not determine encoding"):
            _detect_encoding(path)
    finally:
        os.unlink(path)


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
