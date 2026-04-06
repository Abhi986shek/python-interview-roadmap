"""
Finding the Pivot Index

Find the index where the sum of elements to the left equals
the sum of elements to the right.

Example:
Array: [1, 7, 3, 6, 5, 6] -> Pivot Index: 3
"""

def find_pivot_index(arr):
    total = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        # right sum = total - left_sum - current element
        if left_sum == total - left_sum - num:
            return i
        left_sum += num

    return -1


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = find_pivot_index(arr)

    if result != -1:
        print(f"PIVOT INDEX: {result}")
    else:
        print("NO PIVOT INDEX EXISTS")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
