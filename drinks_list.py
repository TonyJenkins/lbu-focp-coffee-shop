#!/usr/bin/env python3

"""Display a summary of the coffee shop takings."""

import sys
from coffee_shop import full_coffee_name, read_takings_file


def count_the_drinks(transactions):
    drink_counts = {}
    for each_transaction in transactions:
        drink, quantity, price = each_transaction
        if drink in drink_counts:
            drink_counts[drink] += quantity
        else:
            drink_counts[drink] = quantity

    return drink_counts


def print_drinks_table(drink_counts):
    from tabulate import tabulate

    table = [['Drink', 'Count']]
    for each_drink in sorted(drink_counts):
        table.append([full_coffee_name(each_drink), drink_counts[each_drink]])

    print(tabulate(table, headers='firstrow', tablefmt="grid"))


def generate_drinks_list(filename):
    transactions = read_takings_file(filename)
    drink_counts = count_the_drinks(transactions)
    print_drinks_table(drink_counts)
    

if __name__ == "__main__":
    try:
        generate_drinks_list(sys.argv[1])
    except FileNotFoundError:
        print(f"{sys.argv[0]}: cannot open {sys.argv[1]!r}")
    except IndexError:
        print(f"{sys.argv[0]}: no takings file specified")
