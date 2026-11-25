#!/usr/bin/env python3


def read_takings_file(filename):
    """Read a takings file and return each drink, quantity, and unit price."""
    all_takings = []
    with open(filename, "r") as takings_file:
        for transaction in takings_file:
            drink, quantity, unit_price = transaction.strip().split(",")
            all_takings.append(
                (drink, int(quantity), float(unit_price)),
            )

    return all_takings


if __name__ == "__main__":
    pass
