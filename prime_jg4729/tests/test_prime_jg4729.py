from prime_jg4729 import is_prime
import pytest


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
