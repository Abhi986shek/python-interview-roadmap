"""
Maximum Difference

Find the maximum difference arr[j] - arr[i] such that j > i.

Example:
Array: [2, 3, 10, 6, 4, 8, 1] -> Max Difference: 8 (10 - 2)
"""

# def max_difference(arr):
#     if len(arr) < 2:
#         raise ValueError("Array must have at least 2 elements.")

#     min_so_far = arr[0]
#     max_diff = arr[1] - arr[0]

#     for i in range(1, len(arr)):
#         max_diff = max(max_diff, arr[i] - min_so_far)
#         min_so_far = min(min_so_far, arr[i])

#     return max_diff

def max_difference(arr):
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements.")

    max_diff = arr[1] - arr[0]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            difference = arr[j] - arr[i]
            max_diff = max(max_diff, difference)

    return max_diff


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    result = max_difference(arr)
    print(f"MAXIMUM DIFFERENCE (arr[j] - arr[i], j > i): {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
