#!/usr/bin/python3

"""
metrics.py
Description: Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C), print statistics.
"""

import sys

def print_statistics(total_file_size, status_counts):
    """
    Print the computed statistics.

    Args:
        total_file_size (int): The total file size accumulated so far.
        status_counts (dict): A dictionary containing counts of each status code.

    Returns:
        None
    """
    print("Total file size: File size: {}".format(total_file_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_file_size = 0
    status_counts = {}

    try:
        line_number = 0
        for line in sys.stdin:
            line_number += 1
            # Parse the line using the provided input format
            parts = line.split()
            if len(parts) != 9:
                # Skip lines that don't match the format
                continue

            status_code = parts[-3]
            try:
                file_size = int(parts[-1])
            except ValueError:
                # Skip lines where the file size is not an integer
                continue

            # Update the total file size and status code count
            total_file_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_number % 10 == 0:
                # Print statistics after every 10 lines
                print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        # If a keyboard interruption (CTRL + C) occurs, print the current statistics
        print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()

