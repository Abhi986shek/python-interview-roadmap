"""
Two Sum

Find the indices of two numbers in the array that add up to the target.
Uses a hashmap to store seen values for O(1) lookup.

Example:
Array: [2, 7, 11, 15], Target: 9 -> Indices: [0, 1]

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def two_sum(arr, target):
    seen = {}  # value -> index

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    target = int(input("ENTER THE TARGET SUM\n"))

    result = two_sum(arr, target)

    if result:
        i, j = result
        print(f"PAIR FOUND: arr[{i}]={arr[i]} + arr[{j}]={arr[j]} = {target}")
        print(f"INDICES: {result}")
    else:
        print(f"NO PAIR FOUND WITH SUM {target}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
