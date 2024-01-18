#!/usr/bin/python3
'''py module.
'''


def min_operations(n):
    '''optmize the calcylation
    and n operation.
    Returns:
        Integer : number of opration
    '''
    if n <= 1:
        return 0

    min_ops = 0
    current_len = 1
    clipboard = 0

    while current_len < n:
        if n % current_len == 0:
            clipboard = current_len
            min_ops += 1

        current_len += clipboard
        min_ops += 1

    return min_ops
