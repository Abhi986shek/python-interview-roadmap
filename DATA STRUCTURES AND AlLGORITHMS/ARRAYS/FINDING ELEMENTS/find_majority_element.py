"""
Finding the Majority Element (Boyer-Moore Voting Algorithm)

A majority element appears more than n/2 times in the array.
Returns the element if it exists, otherwise reports none found.

Example:
Array: [3, 2, 3] -> Majority: 3
"""

# from collections import Counter

# def find_majority_element(arr):
#     if not arr:
#         return None

#     counts = Counter(arr)

#     for num, count in counts.items():
#         if count > len(arr) // 2:
#             return num

#     return None


def find_majority_element(arr):
    if not arr:
        return None

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count > len(arr) // 2:
            return num

    return None


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = find_majority_element(arr)

    if result is not None:
        print(f"MAJORITY ELEMENT: {result}")
    else:
        print("NO MAJORITY ELEMENT EXISTS")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
