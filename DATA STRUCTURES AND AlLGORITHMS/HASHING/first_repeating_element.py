"""
First Repeating Element

Find the first element in the array that appears more than once.
Uses a hashmap to track frequency in a single pass.

Example:
Array: [5, 3, 4, 1, 3, 5] -> First Repeating: 5 (appears at index 0 and 4)

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def first_repeating(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if freq[num] > 1:
            return num

    return None


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = first_repeating(arr)

    if result is not None:
        print(f"FIRST REPEATING ELEMENT: {result}")
    else:
        print("NO REPEATING ELEMENT FOUND")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
