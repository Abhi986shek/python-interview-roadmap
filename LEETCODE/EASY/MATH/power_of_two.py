"""
Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Example 1:
    Input : n = 1
    Output: True  (2^0 = 1)

Example 2:
    Input : n = 16
    Output: True  (2^4 = 16)

Example 3:
    Input : n = 3
    Output: False

Constraints:
    - -2^31 <= n <= 2^31 - 1

Time Complexity  : O(1)
Space Complexity : O(1)
"""


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


try:
    n = int(input("ENTER THE NUMBER\n"))
    print(f"IS POWER OF TWO: {is_power_of_two(n)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
