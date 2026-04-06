"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it
and return its index. If it does not exist, return -1.

Example 1:
    Input : s = "leetcode"
    Output: 0

Example 2:
    Input : s = "loveleetcode"
    Output: 2

Example 3:
    Input : s = "aabb"
    Output: -1

Constraints:
    - 1 <= s.length <= 10^5
    - s consists of only lowercase English letters

Time Complexity  : O(n)
Space Complexity : O(1)  - at most 26 unique characters
"""

from collections import Counter


def first_uniq_char(s):
    freq = Counter(s)
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1


try:
    s = input("ENTER THE STRING\n")
    if not s:
        raise ValueError("Input cannot be empty.")

    result = first_uniq_char(s)
    if result != -1:
        print(f"FIRST UNIQUE CHARACTER: '{s[result]}' AT INDEX {result}")
    else:
        print("NO UNIQUE CHARACTER FOUND")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
