"""
Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
    Input : n = 10
    Output: 4  (primes: 2, 3, 5, 7)

Example 2:
    Input : n = 0
    Output: 0

Example 3:
    Input : n = 1
    Output: 0

Constraints:
    - 0 <= n <= 5 * 10^6

Time Complexity  : O(n log log n)  - Sieve of Eratosthenes
Space Complexity : O(n)
"""


def count_primes(n):
    if n < 2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    return sum(sieve)


try:
    n = int(input("ENTER N\n"))
    if n < 0:
        raise ValueError("N must be non-negative.")

    print(f"COUNT OF PRIMES LESS THAN {n}: {count_primes(n)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
