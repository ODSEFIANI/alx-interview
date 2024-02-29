#!/usr/bin/python3
'''
py module, dynamic programming
'''
import sys

def minCoins(coins, total):
    '''
    Return: Fewest number of coins needed to meet the total amount.
    
    If the total amount is 0 or less, return 0.
    
    If the total amount cannot be met using any combination of the given coins, return -1.
    
    Parameters:
    - coins (list): A list of coin values.
    - total (int): The target amount.

    Example:
    >>> coins = [1, 2, 5]
    >>> total_amount = 11
    >>> result = minCoins(coins, total_amount)
    >>> print(f"The fewest number of coins needed to make {total_amount} is: {result}")
    '''
    if total <= 0:
        return 0
    dp_table = [sys.maxsize for _ in range(total + 1)]
    dp_table[0] = 0
    coin_count = len(coins)
    for amount in range(1, total + 1):
        for coin_index in range(coin_count):
            if coins[coin_index] <= amount:
                sub_result = dp_table[amount - coins[coin_index]]
                if sub_result != sys.maxsize and sub_result + 1 < dp_table[amount]:
                    dp_table[amount] = sub_result + 1

    if dp_table[total] == sys.maxsize:
        return -1
    return dp_table[total]
