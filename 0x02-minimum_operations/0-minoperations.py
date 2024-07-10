#!/usr/bin/python3
"""
This function counts the number of H in the file.
"""


def minOperations(n):
    """
    Operations to count n number of H in a file
    """
    if n <= 1:
        return
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations