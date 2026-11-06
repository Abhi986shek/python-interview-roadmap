"""
Longest Consecutive Sequence

Find the length of the longest sequence of consecutive integers in the array.

Example:
Array: [100, 4, 200, 1, 3, 2] -> Length: 4 (sequence: 1, 2, 3, 4)
"""

def longest_consecutive(arr):
    arr = sorted(set(arr))

    if not arr:
        return 0

    count = 1
    max_count = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            count += 1
        else:
            count = 1

        max_count = max(max_count, count)

    return max_count


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    print(f"LENGTH OF LONGEST CONSECUTIVE SEQUENCE: {longest_consecutive(arr)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
