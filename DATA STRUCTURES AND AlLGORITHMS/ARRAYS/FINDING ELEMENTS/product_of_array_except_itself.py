"""
Product of Array Except Itself

For each index i, compute the product of all elements except arr[i].
No division allowed.

Example:
Array: [1, 2, 3, 4] -> Output: [24, 12, 8, 6]
"""

def product_except_self(arr):
    result = []

    for i in range(len(arr)):
        product = 1

        for j in range(len(arr)):
            if i != j:
                product *= arr[j]

        result.append(product)

    return result


arr = [1, 2, 3, 4]
print(product_except_self(arr))
