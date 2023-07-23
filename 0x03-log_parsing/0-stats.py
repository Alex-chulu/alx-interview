#!/usr/bin/python3

"""
metrics.py
Description: Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 
HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption 
(CTRL + C), print statistics
"""


import sys


if __name__ == '__main__':
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_statistics():
        """
        Print the computed statistics.

        Args:
        total_file_size (int): The total file size accumulated so far.
        status_counts (dict): A dictionary containing counts 
        of each status code.

        Returns:
            None
        """
        print('Total file size: {}'.format(size[0]))
        for key in sorted(codes.keys()):
            if codes[key]:
                print('{}: {}'.format(key, codes[key]))

    def parse_line(line):
        """ Checks the line for an object """
        try:
            line = line[:-1]
            word = line.split(' ')
            size[0] += int(word[-1])
            code = int(word[-2])
            if code in codes:
                codes[code] += 1
        except BaseException:
            pass

    num = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            if num % 10 == 0:
                print_statistics()
            num += 1
    except KeyboardInterrupt:
        print_statistics()
        raise
    print_statistics()
