#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys


def print_statistics(status_counts, total_size):
    """
    Print statistics based on status counts and total size.
    """
    print("Total file size: {}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        if count != 0:
            print("{}: {}".format(status_code, count))


status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_size += int(parsed_line[0])
                status_code = parsed_line[1]

                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count == 10:
                print_statistics(status_counts, total_size)
                line_count = 0

finally:
    print_statistics(status_counts, total_size)
