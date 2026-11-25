#!/usr/bin/env python3

"""Read transaction data for the coffee shop."""

COFFEE_FULL_NAMES = {
    "espresso": "Espresso",
    "americano": "Americano",
    "macchiato": "Macchiato",
    "flatwhite": "Flat White",
    "latte": "Latte",
    "icedlatte": "Iced Latte",
    "cappuccino": "Cappuccino",
    "mocha": "Mocha",
    "hotchocolate": "Hot Chocolate",
    "tea": "Tea",
}


def read_takings_file(filename):
    """Read takings from a CSV-formatted file."""
    all_takings = []
    with open(filename, "r") as takings_file:
        for transaction in takings_file:
            drink, quantity, unit_price = transaction.strip().split(",")
            all_takings.append(
                (drink, int(quantity), float(unit_price)),
            )

    return all_takings


def full_coffee_name(drink_code):
    """Return a drink code's full name, or the title-cased code."""
    if drink_code in COFFEE_FULL_NAMES:
        return COFFEE_FULL_NAMES[drink_code]

    return drink_code.title()


if __name__ == "__main__":
    pass
