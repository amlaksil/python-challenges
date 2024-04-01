#!/usr/bin/python3
def is_prime(num):
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_pairs(limit):
    """
    Finds all pairs of prime numbers with distances of 2, 4, and 6
    up to a given limit.

    Args:
        limit (int): The upper limit to search for prime pairs.

    Returns:
        tuple: A tuple containing three dictionaries:
            - twin_pairs: Dictionary of twin prime pairs.
            - cousin_pairs: Dictionary of cousin prime pairs.
            - sexy_pairs: Dictionary of sexy prime pairs.
    """
    candidates = [True] * limit
    candidates[0] = candidates[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        for j in range(i*i, limit, i):
            candidates[j] = False

    primes = [num for num, prime in enumerate(candidates) if prime]
    twin_pairs = {}
    cousin_pairs = {}
    sexy_pairs = {}
    for num in primes:
        if num and is_prime(num + 2):
            twin_pairs[num] = num + 2
        if num and is_prime(num + 4):
            cousin_pairs[num] = num + 4
        if num and is_prime(num + 6):
            sexy_pairs[num] = num + 6
    return twin_pairs, cousin_pairs, sexy_pairs


if __name__ == '__main__':
    pairs = prime_pairs(50)
    for pair in pairs:
        print(pair)
