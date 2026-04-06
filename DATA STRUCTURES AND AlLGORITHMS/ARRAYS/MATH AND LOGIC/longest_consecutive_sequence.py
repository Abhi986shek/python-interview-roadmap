"""
Longest Consecutive Sequence

Find the length of the longest sequence of consecutive integers in the array.

Example:
Array: [100, 4, 200, 1, 3, 2] -> Length: 4 (sequence: 1, 2, 3, 4)
"""

def longest_consecutive(arr):
    num_set = set(arr)
    max_length = 0

    for num in num_set:
        # only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


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
