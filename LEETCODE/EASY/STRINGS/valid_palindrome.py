"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input : s = "A man, a plan, a canal: Panama"
    Output: True

Example 2:
    Input : s = "race a car"
    Output: False

Example 3:
    Input : s = " "
    Output: True

Constraints:
    - 1 <= s.length <= 2 * 10^5

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


try:
    s = input("ENTER THE STRING\n")
    print(f"IS PALINDROME: {is_palindrome(s)}")

except Exception as e:
    print(f"An error occurred: {e}")
