"""
Printing the First Non-Repeating Element

Find and print the first element in the array that appears exactly once.

Example:
Array: [9, 4, 9, 6, 7, 4] -> First Non-Repeating: 6
"""

from collections import Counter

def first_non_repeating(arr):
    freq = Counter(arr)

    for num in arr:
        if freq[num] == 1:
            return num

    return None


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = first_non_repeating(arr)

    if result is not None:
        print(f"FIRST NON-REPEATING ELEMENT: {result}")
    else:
        print("ALL ELEMENTS ARE REPEATING")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
