#!/usr/bin/env python3

"""Read transaction data for the coffee shop."""


def read_takings_file(filename):
    """Read transactions from a CSV-formatted takings file.

    Args:
        filename: Path to the takings file.

    Returns:
        A list of ``(drink, quantity, unit_price)`` tuples.
    """
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
