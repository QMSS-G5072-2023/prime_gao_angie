import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

 """
 The is_prime function checks if a given integer is a prime number or not.

    n (int): The integer to be checked for primality.

    It returns boolean: True if the input number is prime, False otherwise.

    Example:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
"""
