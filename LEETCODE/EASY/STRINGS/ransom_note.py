"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.
"""


from collections import Counter

def can_construct(ransom_note, magazine):
    return not (Counter(ransom_note) - Counter(magazine))


try:
    ransom_note = input("ENTER RANSOM NOTE\n")
    magazine = input("ENTER MAGAZINE\n")
    print(f"CAN CONSTRUCT: {can_construct(ransom_note, magazine)}")
except Exception as e:
    print(f"An error occurred: {e}")
