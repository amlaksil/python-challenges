#!/usr/bin/python3
"""
This module contains a function to calculate prime numbers up
to a given limit using the Sieve of Eratosthenes algorithm.
Usage:
    python3 prime_sieve.py [limit]

    - limit (int): The upper limit up to which prime numbers will be
    calculated.

Example:
    python3 prime_sieve.py 50

    This will calculate and print all prime numbers up to 50.
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""
from sys import argv


def cal_primes_up_to(limit):
    """
    Calculates prime numbers up to the specified limit using the Sieve of
    Eratosthenes algorithm.

    Args:
        limit (int): The upper limit up to which prime numbers will be
    calculated.

    Returns:
        primes (list): A list of prime numbers up to the specified limit.

    Algorithm:
        The function utilizes the Sieve of Eratosthenes algorithm to
        efficiently find all prime numbers up to the given limit.
        It initializes a list of boolean values called 'candidates' with
        indices representing numbers from 0 to the limit. Initially, all
        values are set to 'True' to indicate that all numbers are prime
        candidates.

        The function then marks '0' and '1' as non-prime by setting their
        corresponding values in the 'candidates' list to 'False'.
        Starting from 2, it iterates up to the square root of the limit.
        For each prime number 'i' encountered, it marks all its multiples as
        non-prime by setting their corresponding indices in the 'candidates'
        list to 'False'. Finally, it constructs and returns a list of prime
        numbers by filtering the 'candidates' list, including only the numbers
        marked as 'True'.
    Example:
        >>> cal_primes_up_to(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    candidates = [True] * limit
    candidates[0] = candidates[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        for j in range(i*i, limit, i):
            candidates[j] = False
    return [num for num, prime in enumerate(candidates) if prime]


if __name__ == '__main__':
    print(cal_primes_up_to(int(argv[1])))
