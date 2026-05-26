from trees import extract_street_names, load_tree_categories


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
