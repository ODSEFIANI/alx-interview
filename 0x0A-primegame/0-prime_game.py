#!/usr/bin/python3
"""Prime game module"""


def is_prime(num):
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def optimal_move(n):
    """
    Determines the optimal move for a given round.

    Args:
        n (int): The upper bound of the consecutive integers.

    Returns:
        int or None: The optimal move (prime number)
    """
    # Maria always chooses 2 if it's available
    if n > 2:
        return 2
    # If 2 is not available, choose the smallest prime available
    for i in range(3, n + 1):
        if is_prime(i):
            return i
    return None


def isWinner(x, nums):
    """
    Determines the winner of the prime game for multiple rounds.

    Args:
        x (int): The number of rounds.
    nums (list): A list of integers representing the values of

    Returns:
        str or None: The name of the player that won the mo
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        # Count the number of primes in the range [1, n]
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        # If the number of primes is even, Ben wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    # Determine the winner based on the number of wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
