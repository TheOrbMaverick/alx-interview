#!/usr/bin/python3
"""
This is the prime game
"""


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    # Find maximum n from nums to limit the sieve
    max_n = max(nums)

    # Sieve of Eratosthenes to determine all primes up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each number n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 1:  # Maria wins if the number of primes up to n is odd
            maria_wins += 1
        else:  # Ben wins if the number of primes up to n is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

