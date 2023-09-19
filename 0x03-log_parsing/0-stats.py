#!/usr/bin/python3
"""log parsing in Python
"""
import sys
import re


# Initialize variables to store metrics
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        # Use regular expressions to parse the log line
        match = re.match(r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)

        if match:
            ip, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            # Update total file size
            total_file_size += file_size

            # Update status code count
            if status_code in status_codes:
                status_codes[status_code] += 1

        # Print statistics after every 10 lines or on keyboard interruption
        if line_count % 10 == 0:
            print("Total file size: File size:", total_file_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    pass

# Print the final statistics
print("Total file size: File size:", total_file_size)
for code in sorted(status_codes.keys()):
    if status_codes[code] > 0:
        print(f"{code}: {status_codes[code]}")
