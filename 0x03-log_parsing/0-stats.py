#!/usr/bin/python3
"""log parsing in Python
"""
import sys


# Print statistics after every 10 lines or on keyboard interruption
def print_data(total_file_size, status_code_d):
    """prints total size and status code count"""
    print('File size: {}'.format(total_file_size))
    for k, v in sorted(status_code_d.items()):
        if v != 0:
            print('{}: {}'.format(k, v))


# Initialize variables to store metrics
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_code_d = {cd: 0 for cd in status_codes}
total_file_size = 0
try:
    count = 0
    # Use regular expressions to parse the log line
    for line in sys.stdin:
        splitstr = line.split()
        try:
            # Update total file size
            total_file_size += int(splitstr[-1])
            # Update status code count
            cd = splitstr[-2]
            if cd in status_code_d:
                count += 1
                status_code_d[cd] += 1
                if count % 10 == 0:
                    print_data(total_file_size, status_code_d)
        except:
            pass
except KeyboardInterrupt:
    print_data(total_file_size, status_code_d)
    raise
else:
    print_data(total_file_size, status_code_d)
