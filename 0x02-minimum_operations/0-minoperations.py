#!/usr/bin/env python3
'''py module
'''
import math


def minOperations(n):
    """Minimum Operations Function"""

    def custom_round(number):
        """Round up"""
        decimal_part = number - int(number)  # Extract the decimal part

        if decimal_part < 0.50:
            return int(number)  # Round down
        else:
            return int(number) + 1  # Round up

    if n <= 1:
        return 0
    if n % 2 == 0:
        p = custom_round(math.log(n, 2) * 2)
    else:
        p = custom_round(math.log((n-1), 2) * 2)
    return p
