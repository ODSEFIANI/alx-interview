#!/usr/bin/python3

import sys


def print_msg(di_ct, fileSize):
    """
    Method py
    """

    print("File size: {}".format(fileSize))
    for a, b in sorted(di_ct.items()):
        if b != 0:
            print("{}: {}".format(a, b))


fileSize = 0
c_od = 0
co_unter = 0
di_ct = {"200": 0,
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
            co_unter += 1

            if co_unter <= 10:
                fileSize += int(parsed_line[0])
                c_od = parsed_line[1]

                if (c_od in di_ct.keys()):
                    di_ct[c_od] += 1

            if (co_unter == 10):
                print_msg(di_ct, fileSize)
                co_unter = 0

finally:
    print_msg(di_ct, fileSize)
