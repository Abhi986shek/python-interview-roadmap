"""
Next Greater Element

For each element in the array, find the next element to its right that is greater.
If no such element exists, output -1.

Example:
Input : [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        # pop elements smaller than current — current is their next greater
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = next_greater_element(arr)

    print("ELEMENT -> NEXT GREATER ELEMENT")
    for i in range(len(arr)):
        print(f"  {arr[i]} -> {result[i]}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
