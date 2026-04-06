"""
Merge Two Sorted Arrays

Merge two sorted arrays into a single sorted array without using built-in sort.

Example:
Array 1: [1, 3, 5]
Array 2: [2, 4, 6]
Merged:  [1, 2, 3, 4, 5, 6]
"""

def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


try:
    raw1 = input("ENTER THE FIRST SORTED ARRAY (space separated)\n")
    raw2 = input("ENTER THE SECOND SORTED ARRAY (space separated)\n")

    arr1 = list(map(int, raw1.split()))
    arr2 = list(map(int, raw2.split()))

    if not arr1 or not arr2:
        raise ValueError("Both arrays must have at least one element.")

    result = merge_sorted_arrays(arr1, arr2)
    print(f"MERGED SORTED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
