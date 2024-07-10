#!/usr/bin/python3
"""Module for Minimum operations algorithm"""


def minOperations(n):
    """
    Calculates fewest number of operations
    """

    if n is None or n < 1:
        return 0
    operations = 0
    factors = 2
    while factors <= n:
        while n % factors == 0:
            operations += factors
            n //= factors
        factors += 1

    return operations
