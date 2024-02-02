#!/usr/bin/python3
"""
UTF-8
"""


def validUTF8(data):
    """function
    """
    by_ct = 0

    for i in data:
        if by_ct == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                by_ct = 1
            elif i >> 4 == 0b1110:
                by_ct = 2
            elif i >> 3 == 0b11110:
                by_ct = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            by_ct -= 1
    return by_ct == 0
