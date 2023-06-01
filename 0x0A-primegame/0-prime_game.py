#!/usr/bin/python3
"""Display Prime Game"""


def isWinner(x, nums):
    """Display the winner"""
    def isPrime(num):
        """Display prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def playGame(n):
        """Define play game"""
        if n == 1:
            return False

        primes = []
        for i in range(2, n + 1):
            if isPrime(i):
                primes.append(i)

        if len(primes) % 2 == 0:
            return False
        else:
            return True

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        if playGame(nums[i]):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
