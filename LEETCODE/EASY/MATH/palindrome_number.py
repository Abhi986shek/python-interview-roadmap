"""
Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same forward and backward.

Example 1:
    Input : x = 121
    Output: True

Example 2:
    Input : x = -121
    Output: False  (reads as 121- from right, not a palindrome)

Example 3:
    Input : x = 10
    Output: False

Constraints:
    - -2^31 <= x <= 2^31 - 1

Time Complexity  : O(log n)
Space Complexity : O(1)
"""


def is_palindrome(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]


try:
    x = int(input("ENTER THE NUMBER\n"))
    print(f"IS PALINDROME: {is_palindrome(x)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
