import sys

from trees import calculate_average_price, load_properties, load_tree_categories


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python main.py <trees-json> <property-csv>", file=sys.stderr)
        sys.exit(1)

    trees_path, csv_path = sys.argv[1], sys.argv[2]

    short_streets, tall_streets = load_tree_categories(trees_path)
    properties = load_properties(csv_path)

    short_avg = calculate_average_price(properties, short_streets)
    tall_avg = calculate_average_price(properties, tall_streets)

    print(f"Average property price on streets with short trees: €{short_avg:,.2f}")
    print(f"Average property price on streets with tall trees:  €{tall_avg:,.2f}")


if __name__ == "__main__":
    main()
