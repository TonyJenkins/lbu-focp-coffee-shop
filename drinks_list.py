#!/usr/bin/env python3

"""Display a summary of the coffee shop takings."""

import sys
from coffee_shop import full_coffee_name, read_takings_file


def count_the_drinks(transactions):
    """Count quantities and values for each drink."""
    drink_counts = {}
    drink_values = {}

    for each_transaction in transactions:
        drink, quantity, price = each_transaction
        if drink in drink_counts:
            drink_counts[drink] += quantity
            drink_values[drink] += quantity * price
        else:
            drink_counts[drink] = quantity
            drink_values[drink] = quantity * price

    return drink_counts, drink_values


def print_drinks_table(drink_counts, drink_values):
    """Print a table of drink quantities and total values."""
    from tabulate import tabulate

    table = [["Drink", "Count", "Total Value"]]
    for each_drink in sorted(drink_counts):
        table.append(
            [
                full_coffee_name(each_drink),
                drink_counts[each_drink],
                f"£{drink_values[each_drink]:7.2f}",
            ]
        )

    print(tabulate(table, headers="firstrow", tablefmt="grid"))


def generate_drinks_list(filename):
    """Read takings data and print a drink summary."""
    transactions = read_takings_file(filename)
    drink_counts, drink_values = count_the_drinks(transactions)
    print_drinks_table(drink_counts, drink_values)


if __name__ == "__main__":
    try:
        generate_drinks_list(sys.argv[1])
    except FileNotFoundError:
        print(f"{sys.argv[0]}: cannot open {sys.argv[1]!r}")
    except IndexError:
        print(f"{sys.argv[0]}: no takings file specified")
