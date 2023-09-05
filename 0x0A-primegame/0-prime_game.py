#!/usr/bin/python3
"""
isWinner - Determine the winner of a prime number game.
"""

def isWinner(x, nums):
    """
    Determine the winner of the prime number game.

    Args:
    - x: The number of rounds to be played.
    - nums: An array of integers representing the range of numbers for each round.

    Returns:
    - The name of the player that won the most rounds.
    - If the winner cannot be determined, return None.
    """
    def is_prime(n):
        """
        Check if a number is prime.

        Args:
        - n: The number to check for primality.

        Returns:
        - True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_winner(n):
        """
        Find the winner of a single round.

        Args:
        - n: The upper limit of the number range for this round.

        Returns:
        - The name of the player that wins this round.
        """
        maria_turn = True  # Maria goes first

        while n >= 2:
            prime_found = False

            # Find the largest prime number in the range [2, n]
            for i in range(n, 1, -1):
                if is_prime(i):
                    prime_found = True
                    n -= i  # Remove the prime number and its multiples
                    break

            if not prime_found:
                break

            maria_turn = not maria_turn  # Switch turns

        return "Maria" if maria_turn else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = find_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"

