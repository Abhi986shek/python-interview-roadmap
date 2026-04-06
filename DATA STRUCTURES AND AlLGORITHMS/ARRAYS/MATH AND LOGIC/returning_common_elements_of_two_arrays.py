"""
Returning Common Elements of Two Arrays

Find all elements that appear in both arrays (intersection), without duplicates.

Example:
Array 1: [1, 2, 3, 4, 5]
Array 2: [3, 4, 5, 6, 7]
Common:  [3, 4, 5]
"""

def common_elements(arr1, arr2):
    return sorted(set(arr1) & set(arr2))


try:
    raw1 = input("ENTER THE FIRST ARRAY (space separated)\n")
    raw2 = input("ENTER THE SECOND ARRAY (space separated)\n")

    arr1 = list(map(int, raw1.split()))
    arr2 = list(map(int, raw2.split()))

    if not arr1 or not arr2:
        raise ValueError("Both arrays must have at least one element.")

    result = common_elements(arr1, arr2)

    if result:
        print(f"COMMON ELEMENTS: {result}")
    else:
        print("NO COMMON ELEMENTS FOUND")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
