from prime_jg4729 import is_prime
import pytest

def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False

def test_generate_primes():
    assert generate_primes(1) == []
    assert generate_primes(2) == [2]
    assert generate_primes(10) == [2, 3, 5, 7]
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
