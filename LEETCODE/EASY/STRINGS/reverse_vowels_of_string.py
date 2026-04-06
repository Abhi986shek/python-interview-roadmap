"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consist of printable ASCII characters.
"""


def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)


try:
    s = input("ENTER STRING\n")
    print(f"RESULT: {reverse_vowels(s)}")
except Exception as e:
    print(f"An error occurred: {e}")
