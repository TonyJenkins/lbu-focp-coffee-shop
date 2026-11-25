#!/usr/bin/env python3


def read_takings_file(filename):
    all_takings = []
    with open(filename, 'r') as takings_file:
        for transaction in takings_file:
            drink, quantity, unit_price = transaction.strip().split(',')
            all_takings.append((drink, int(quantity), float(unit_price)),)

    return all_takings


def calculate_total_taking(all_takings):
    total_takings = 0.0
    for each_transaction in all_takings:
        drink, number_sold, unit_price = each_transaction
        total_takings += number_sold * unit_price

    return total_takings


def display_total_takings(filename):
    all_the_takings = read_takings_file(filename)
    print(f'Total Takings: £{calculate_total_taking(all_the_takings):.2f}')


if __name__ == '__main__':
    display_total_takings('data/friday.csv')
