#!/usr/bin/python3

"""
Calculates the fewest number of operations 
needed to obtain exactly n 'H' characters in a file,
using the Copy All and Paste operations.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed 
    to obtain exactly n 'H' characters in a file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations required. 
        Returns 0 if n is impossible to achieve.
    """
    if n == 0:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations

