#!/usr/bin/python3

"""
metrics.py
Description: Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 
HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption 
(CTRL + C), print statistics.
"""

import sys

def print_statistics(file_size, codes):
    """
    Print the computed statistics.

    Args:
        total_file_size (int): The total file size accumulated so far.
        status_counts (dict): A dictionary containing counts 
        of each status code.

    Returns:
        None
    """
    print("Total file size: File size: {}".format(file_size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))

if __name__ == "__main__":
    import sys

    file_size = 0
    codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(file_size, codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if codes.get(line[-2], -1) == -1:
                        [line[-2]] = 1
                    else:
                        codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, codes)

    except KeyboardInterrupt:
        print_stats(file_size, codes)
        raise

