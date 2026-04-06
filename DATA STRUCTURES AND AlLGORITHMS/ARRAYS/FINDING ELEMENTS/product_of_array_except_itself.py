"""
Product of Array Except Itself

For each index i, compute the product of all elements except arr[i].
No division allowed.

Example:
Array: [1, 2, 3, 4] -> Output: [24, 12, 8, 6]
"""

def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    # left pass: result[i] = product of all elements to the left of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    # right pass: multiply by product of all elements to the right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    print(f"PRODUCT ARRAY EXCEPT SELF: {product_except_self(arr)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
