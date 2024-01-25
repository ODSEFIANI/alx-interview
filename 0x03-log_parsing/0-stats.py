#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


def extract_info(line):
    """
    Extracts status code and file size information from a log line.

    Args:
    - line (str): A log line containing status code and file size.

    Returns:
    - dict or None: A dictionary containing status code and file size if valid,
      or None if the line format is invalid.
    """
    parts = line.split()
    if len(parts) >= 7:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return {'status_code': status_code, 'file_size': file_size}
    return None

def print_stats(total_size, status_counts):
    """
    Prints file size and status code statistics.

    Args:
    - total_size (int): Total file size.
    - status_counts (dict): A dictionary containing counts for each status code.
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")

def main():
    """
    Main function to read stdin, compute metrics, and print statistics.
    """
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            try:
                info = extract_info(line)
                if info:
                    status_code = info['status_code']
                    file_size = info['file_size']

                    total_size += file_size

                    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        status_counts.setdefault(status_code, 0)
                        status_counts[status_code] += 1

                    if i % 10 == 0:
                        print_stats(total_size, status_counts)

            except ValueError:
                # Skip lines with invalid status codes or file sizes
                pass

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
