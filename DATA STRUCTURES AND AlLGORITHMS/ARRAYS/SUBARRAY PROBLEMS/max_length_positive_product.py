"""
Max Length Subarray with Positive Product

Find the length of the longest subarray where the product of all elements is positive.

Example:
Array: [1, -2, -3, 4] -> Length: 4 (product = 24, positive)
"""

def max_length_positive_product(arr):
    n = len(arr)
    max_len = 0

    # pos = length of current subarray with positive product
    # neg = length of current subarray with negative product
    pos, neg = 0, 0

    for num in arr:
        if num == 0:
            pos, neg = 0, 0
        elif num > 0:
            pos += 1
            neg = neg + 1 if neg > 0 else 0
        else:
            pos, neg = neg + 1 if neg > 0 else 0, pos + 1

        max_len = max(max_len, pos)

    return max_len


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = max_length_positive_product(arr)
    print(f"MAX LENGTH SUBARRAY WITH POSITIVE PRODUCT: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
