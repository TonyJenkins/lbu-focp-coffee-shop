#!/usr/bin/env python3

"""Utilities for extracting information from coffee shop filenames."""

import calendar


def day_found_in_filename(filename):
    """Return the full weekday name found in a CSV filename.

    Return ``None`` when the filename contains no recognised weekday.
    """
    for day in list(calendar.day_name):
        if day.lower() in filename.lower():
            return day

    return None


if __name__ == "__main__":

    print(day_found_in_filename("wednesday.csv"))
    print(day_found_in_filename("wodinsday.csv"))
