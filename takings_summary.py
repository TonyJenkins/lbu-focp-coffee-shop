#!/usr/bin/env python3

"""Display a summary of the coffee shop takings."""

import sys
from coffee_shop import read_takings_file
from utils import day_found_in_filename


def calculate_total_taking(all_takings):
    """Calculate the total revenue."""
    total_takings = 0.0
    for each_transaction in all_takings:
        _, number_sold, unit_price = each_transaction
        total_takings += number_sold * unit_price

    return total_takings


def calculate_transaction_count(all_takings):
    """Return the transaction count."""
    return len(all_takings)


def calculate_average_transaction_value(all_takings):
    """Calculate the average transaction value."""
    return calculate_total_taking(all_takings) / calculate_transaction_count(
        all_takings
    )


def display_takings_summary(filename):
    """Read a takings file and display the summary."""
    all_the_takings = read_takings_file(filename)
    day = day_found_in_filename(filename)
    if day:
        print(f"Takings for {day}")
    else:
        print(f"Takings from {filename!r}")

    print()
    print(f"Transaction Count: {calculate_transaction_count(all_the_takings)}")
    print(f"Total Takings:     £{calculate_total_taking(all_the_takings):.2f}")
    print(
        f"Average Take:      £{calculate_average_transaction_value(all_the_takings):.2f}"
    )


if __name__ == "__main__":
    try:
        display_takings_summary(sys.argv[1])
    except FileNotFoundError:
        print(f"{sys.argv[0]}: cannot open {sys.argv[1]!r}")
    except IndexError:
        print(f"{sys.argv[0]}: no takings file specified")
