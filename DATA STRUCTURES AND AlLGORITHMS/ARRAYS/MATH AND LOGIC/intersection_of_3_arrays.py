"""
Intersection of 3 Arrays

Find all elements that are common in all three arrays.

Example:
Array 1: [1, 5, 10, 20, 40, 80]
Array 2: [6, 7, 20, 80, 100]
Array 3: [3, 4, 15, 20, 30, 70, 80, 120]
Intersection: [20, 80]
"""

def intersection_of_three(arr1, arr2, arr3):
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)
    return sorted(set1 & set2 & set3)


try:
    raw1 = input("ENTER FIRST ARRAY (space separated)\n")
    raw2 = input("ENTER SECOND ARRAY (space separated)\n")
    raw3 = input("ENTER THIRD ARRAY (space separated)\n")

    arr1 = list(map(int, raw1.split()))
    arr2 = list(map(int, raw2.split()))
    arr3 = list(map(int, raw3.split()))

    if not arr1 or not arr2 or not arr3:
        raise ValueError("All three arrays must have at least one element.")

    result = intersection_of_three(arr1, arr2, arr3)

    if result:
        print(f"INTERSECTION: {result}")
    else:
        print("NO COMMON ELEMENTS FOUND")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
