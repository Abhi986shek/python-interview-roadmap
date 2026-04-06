"""
Minimum Moves to Equal Elements

Find the minimum number of moves to make all elements equal.
Each move increments all elements except one by 1.
This is equivalent to finding the sum of differences from the minimum.

Example:
Array: [1, 2, 3] -> 3 moves
"""

def min_moves_to_equal(arr):
    min_val = min(arr)
    return sum(num - min_val for num in arr)


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    print(f"MINIMUM MOVES TO MAKE ALL ELEMENTS EQUAL: {min_moves_to_equal(arr)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
