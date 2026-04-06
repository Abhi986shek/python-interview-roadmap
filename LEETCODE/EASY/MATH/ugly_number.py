"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
- -2^31 <= n <= 2^31 - 1
"""


def is_ugly(n):
    if n <= 0:
        return False
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1


try:
    n = int(input("ENTER N\n"))
    print(f"IS UGLY NUMBER: {is_ugly(n)}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
