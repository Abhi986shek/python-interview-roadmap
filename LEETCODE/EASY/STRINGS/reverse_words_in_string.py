"""
Reverse Words in a String III

Given a string s, reverse the order of characters in each word within
a sentence while still preserving whitespace and initial word order.

Example 1:
    Input : s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoC"

Example 2:
    Input : s = "Mr Ding"
    Output: "rM gniD"

Constraints:
    - 1 <= s.length <= 5 * 10^4
    - s contains printable ASCII characters
    - There are no leading or trailing spaces

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())


try:
    s = input("ENTER THE STRING\n")
    if not s.strip():
        raise ValueError("Input cannot be empty.")

    print(f"RESULT: {reverse_words(s)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
