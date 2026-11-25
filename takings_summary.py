#!/usr/bin/env python3

"""Read coffee takings data and display the total revenue."""

import sys
from coffee_shop import read_takings_file


def calculate_total_taking(all_takings):
    """Calculate and return the total revenue from the takings."""
    total_takings = 0.0
    for each_transaction in all_takings:
        _, number_sold, unit_price = each_transaction
        total_takings += number_sold * unit_price

    return total_takings


def display_total_takings(filename):
    """Read the takings file and print the formatted total revenue."""
    all_the_takings = read_takings_file(filename)
    print(f"Total Takings: £{calculate_total_taking(all_the_takings):.2f}")


if __name__ == "__main__":
    try:
        display_total_takings(sys.argv[1])
    except FileNotFoundError:
        print(f"{sys.argv[0]}: cannot open {sys.argv[1]!r}")
    except IndexError:
        print(f"{sys.argv[0]}: no takings file specified")
