#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def min_operations(n):
    """optimztion
    """
    current_chars = 1
    clibBd = 0
    operations_counter = 0

    while current_chars < n:
        if clibBd == 0:
            clibBd = current_chars
            operations_counter += 1

        if current_chars == 1:
            current_chars += clibBd
            operations_counter += 1
            continue

        remaining_chars = n - current_chars

        if remaining_chars < clibBd:
            return 0

        if remaining_chars % current_chars != 0:
            current_chars += clibBd
            operations_counter += 1
        else:
            clibBd = current_chars
            current_chars += clibBd
            operations_counter += 2

    if current_chars == n:
        return operations_counter
    else:
        return 0
