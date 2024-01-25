#!/usr/bin/python3
'''py module
'''
import sys


def print_stats(total_size, status_codes):
    """py function"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def main():
    """py function"""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            try:
                parts = line.split()
                if len(parts) >= 7:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])

                    total_size += file_size

                    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        if status_code not in status_codes:
                            status_codes[status_code] = 0
                        status_codes[status_code] += 1

                    if i % 10 == 0:
                        print_stats(total_size, status_codes)

            except ValueError:
                # Skip lines with invalid status codes or file sizes
                pass

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
