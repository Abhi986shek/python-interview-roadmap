"""
Minimum Distance Between Two Numbers

Find the minimum distance (index difference) between two given numbers in the array.

Example:
Array: [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3], x = 3, y = 6 -> Min Distance: 4
"""

def min_distance(arr, x, y):
    last_x = last_y = -1
    min_dist = float('inf')

    for i, num in enumerate(arr):
        if num == x:
            last_x = i
        elif num == y:
            last_y = i

        if last_x != -1 and last_y != -1:
            min_dist = min(min_dist, abs(last_x - last_y))

    return min_dist if min_dist != float('inf') else -1


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    x = int(input("ENTER THE FIRST NUMBER\n"))
    y = int(input("ENTER THE SECOND NUMBER\n"))

    if x == y:
        raise ValueError("Both numbers must be different.")

    result = min_distance(arr, x, y)

    if result != -1:
        print(f"MINIMUM DISTANCE BETWEEN {x} AND {y}: {result}")
    else:
        print(f"ONE OR BOTH NUMBERS NOT FOUND IN THE ARRAY")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
