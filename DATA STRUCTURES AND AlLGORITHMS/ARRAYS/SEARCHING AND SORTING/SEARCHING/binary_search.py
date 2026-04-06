"""
Binary Search

Works only on sorted arrays. Repeatedly divides the search space in half
by comparing the target with the middle element.

Time Complexity:
    Best    : O(1)      - target is the middle element
    Average : O(log n)
    Worst   : O(log n)

Space Complexity:
    Iterative : O(1)
    Recursive : O(log n) - call stack
"""

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


try:
    raw = input("ENTER THE SORTED ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    target = int(input("ENTER THE TARGET VALUE\n"))

    choice = input("USE ITERATIVE OR RECURSIVE? (i/r)\n").strip().lower()

    if choice == 'r':
        result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    else:
        result = binary_search_iterative(arr, target)

    if result != -1:
        print(f"TARGET {target} FOUND AT INDEX {result}")
    else:
        print(f"TARGET {target} NOT FOUND IN THE ARRAY")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
