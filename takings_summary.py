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


def calculate_transaction_count(all_takings):
    return len(all_takings)


def calculate_average_transaction_value(all_takings):
    return calculate_total_taking(all_takings) / calculate_transaction_count(all_takings)


def display_takings_summary(filename):
    """Read the takings file and print the formatted total revenue."""
    all_the_takings = read_takings_file(filename)
    print(f'Transaction Count: {calculate_transaction_count(all_the_takings)}')
    print(f"Total Takings:     £{calculate_total_taking(all_the_takings):.2f}")
    print(f'Average Take:      £{calculate_average_transaction_value(all_the_takings):.2f}')


if __name__ == "__main__":
    try:
        display_takings_summary(sys.argv[1])
    except FileNotFoundError:
        print(f"{sys.argv[0]}: cannot open {sys.argv[1]!r}")
    except IndexError:
        print(f"{sys.argv[0]}: no takings file specified")
