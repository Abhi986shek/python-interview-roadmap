"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input : strs = ["flower", "flow", "flight"]
    Output: "fl"

Example 2:
    Input : strs = ["dog", "racecar", "car"]
    Output: ""

Constraints:
    - 1 <= strs.length <= 200
    - 0 <= strs[i].length <= 200
    - strs[i] consists of only lowercase English letters

Time Complexity  : O(n * m)  - n = number of strings, m = length of shortest string
Space Complexity : O(1)
"""


def longest_common_prefix(strs):
    if not strs:
        return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]


try:
    raw = input("ENTER STRINGS (comma separated)\n")
    strs = [s.strip() for s in raw.split(",")]

    if not strs:
        raise ValueError("Input cannot be empty.")

    result = longest_common_prefix(strs)
    print(f"LONGEST COMMON PREFIX: '{result}'" if result else "NO COMMON PREFIX")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
