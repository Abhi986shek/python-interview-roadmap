"""
Find the Duplicate Elements

Print all elements that appear more than once in the array.

Example:
Array: [4, 3, 2, 7, 8, 2, 3, 1] -> Duplicates: [2, 3]
"""

def find_duplicates(arr):
    seen = set()
    duplicates = []

    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)

    return duplicates


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = find_duplicates(arr)

    if result:
        print(f"DUPLICATE ELEMENTS: {result}")
    else:
        print("NO DUPLICATE ELEMENTS FOUND")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
