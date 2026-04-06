"""
Maximum Product of a Subarray

Find the contiguous subarray that has the largest product.

Example:
Array: [2, 3, -2, 4] -> Max Product: 6 (subarray [2, 3])
"""

def max_product_subarray(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        # when multiplied by a negative, max becomes min and vice versa
        if arr[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(arr[i], max_prod * arr[i])
        min_prod = min(arr[i], min_prod * arr[i])

        result = max(result, max_prod)

    return result


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    print(f"MAXIMUM PRODUCT OF A SUBARRAY: {max_product_subarray(arr)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
