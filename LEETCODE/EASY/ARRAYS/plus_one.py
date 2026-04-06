"""
Plus One

You are given a large integer represented as an integer array digits,
where each digits[i] is the i-th digit of the integer.
The digits are ordered from most significant to least significant.
Increment the large integer by one and return the resulting array.

Example 1:
    Input : digits = [1, 2, 3]
    Output: [1, 2, 4]

Example 2:
    Input : digits = [9]
    Output: [1, 0]

Example 3:
    Input : digits = [9, 9]
    Output: [1, 0, 0]

Constraints:
    - 1 <= digits.length <= 100
    - digits[i] is a digit 0-9

Time Complexity  : O(n)
Space Complexity : O(1)
"""


def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


try:
    raw = input("ENTER DIGITS (space separated)\n")
    digits = list(map(int, raw.split()))

    if not digits:
        raise ValueError("Digits cannot be empty.")

    if any(d < 0 or d > 9 for d in digits):
        raise ValueError("Each digit must be between 0 and 9.")

    print(f"RESULT: {plus_one(digits)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
