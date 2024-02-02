#!/usr/bin/python3

import sys


def print_msg(dc, fileSize):
    """
    Method to print
    """

    print("File size: {}".format(fileSize))
    for k, v in sorted(dc.items()):
        if v != 0:
            print("{}: {}".format(k, v))


fileSize = 0
code = 0
count = 0
dc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                fileSize += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dc.keys()):
                    dc[code] += 1

            if (count == 10):
                print_msg(dc, fileSize)
                count = 0

finally:
    print_msg(dc, fileSize)