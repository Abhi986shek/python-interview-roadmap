"""
Reverse String

Write a function that reverses a string.
The input is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input : s = ['h', 'e', 'l', 'l', 'o']
    Output: ['o', 'l', 'l', 'e', 'h']

Example 2:
    Input : s = ['H', 'a', 'n', 'n', 'a', 'h']
    Output: ['h', 'a', 'n', 'n', 'a', 'H']

Constraints:
    - 1 <= s.length <= 10^5

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


try:
    raw = input("ENTER THE STRING\n")
    if not raw:
        raise ValueError("Input cannot be empty.")

    s = list(raw)
    reverse_string(s)
    print(f"REVERSED: {''.join(s)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
