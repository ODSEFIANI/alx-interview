#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys
import re

def parse_log_line(line):
    """
    Parses a log line and extracts IP, status code, and file size.

    Args:
    - line (str): A log line.

    Returns:
    - tuple: A tuple containing IP, status code, and file size.
    """
    log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (?P<status_code>\d+) (?P<file_size>\d+)'
    match = re.match(log_pattern, line)
    if match:
        ip = match.group('ip')
        status_code = int(match.group('status_code'))
        file_size = int(match.group('file_size'))
        return ip, status_code, file_size
    return None

def print_statistics(total_size, status_counts):
    """
    Prints file size and status code statistics.

    Args:
    - total_size (int): Total file size.
    - status_counts (dict): A dictionary containing counts for each status code.
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            log_info = parse_log_line(line)
            if log_info:
                ip, status_code, file_size = log_info

                total_size += file_size

                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_counts.setdefault(status_code, 0)
                    status_counts[status_code] += 1

                if i % 10 == 0:
                    print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
