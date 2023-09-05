#!/usr/bin/python3

def isWinner(x, nums):
    if not x or not nums:
        return None

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_winner(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        if len(primes) % 2 == 0:
            return "Ben"
        return "Maria"

    winners = [calculate_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print("Winner: {}".format(isWinner(x, nums)))

