#!/usr/bin/python3

import sys

def print_statistics(total_size, status_codes):
    """
    Prints the total file size and the count of each status code.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing status codes as keys and their counts as values.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        if count > 0:
            print("{}: {}".format(code, count))

def main():
    """
    Main function to read and process log lines from stdin.

    Reads log lines from stdin, extracts information such as status code and file size, and calculates statistics.
    """
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split()
            if len(tokens) > 7:
                status_code = tokens[-2]
                file_size = tokens[-1]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += int(file_size)

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()

