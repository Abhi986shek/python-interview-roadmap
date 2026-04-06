"""
Count Vowel Substrings of a String

A substring is a contiguous sequence of characters within a string.
Given a string word, return the number of vowel substrings in word.
A vowel substring is a substring that only consists of vowels
('a', 'e', 'i', 'o', 'u') and has all five vowels present in it.

Example 1:
    Input : word = "aeiouu"
    Output: 2
    Explanation: "aeiou" and "aeiouu" are vowel substrings.

Example 2:
    Input : word = "unicornarihan"
    Output: 0

Example 3:
    Input : word = "cuaieuouac"
    Output: 7

Constraints:
    - 1 <= word.length <= 100
    - word consists of lowercase English letters only

Time Complexity  : O(n²)
Space Complexity : O(1)
"""


def count_vowel_substrings(word):
    vowels = set('aeiou')
    count = 0
    n = len(word)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if word[j] not in vowels:
                break
            seen.add(word[j])
            if len(seen) == 5:
                count += 1

    return count


try:
    word = input("ENTER THE STRING\n")
    if not word:
        raise ValueError("Input cannot be empty.")

    print(f"COUNT OF VOWEL SUBSTRINGS: {count_vowel_substrings(word)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
