"""
Rearranging the Array Alternatively

Rearrange so that the array alternates between the largest and smallest
remaining elements.

Example:
Array: [1, 2, 3, 4, 5] -> [5, 1, 4, 2, 3]
"""

def rearrange_alternatively(arr):
    arr.sort()
    result = []
    left, right = 0, len(arr) - 1

    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])
        left += 1
        right -= 1

    return result


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = rearrange_alternatively(arr)
    print(f"REARRANGED ARRAY: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
