"""
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-2^31, 2^31 - 1], then return 0.

Example 1:
    Input : x = 123
    Output: 321

Example 2:
    Input : x = -123
    Output: -321

Example 3:
    Input : x = 120
    Output: 21

Constraints:
    - -2^31 <= x <= 2^31 - 1

Time Complexity  : O(log x)
Space Complexity : O(1)
"""


def reverse(x):
    sign = -1 if x < 0 else 1
    rev = int(str(abs(x))[::-1]) * sign
    if rev < -(2**31) or rev > 2**31 - 1:
        return 0
    return rev


try:
    x = int(input("ENTER THE INTEGER\n"))
    print(f"REVERSED: {reverse(x)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
