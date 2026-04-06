"""
Linear Search

Checks every element one by one from left to right until the target is found.
Works on both sorted and unsorted arrays.

Time Complexity:
    Best    : O(1)  - target is the first element
    Average : O(n)
    Worst   : O(n)  - target is the last element or not present

Space Complexity: O(1)
"""

def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    target = int(input("ENTER THE TARGET VALUE\n"))

    result = linear_search(arr, target)

    if result != -1:
        print(f"TARGET {target} FOUND AT INDEX {result}")
    else:
        print(f"TARGET {target} NOT FOUND IN THE ARRAY")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
