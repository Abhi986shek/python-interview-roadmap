"""
Area of a Container Which Can Contain Maximum Amount of Water

Given heights of vertical lines, find two lines that together with the x-axis
forms a container that holds the most water.

Example:
Heights: [1, 8, 6, 2, 5, 4, 8, 3, 7] -> Max Area: 49
"""

def max_water_container(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        max_area = max(max_area, height * width)

        # move the pointer with the shorter line inward
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


try:
    raw = input("ENTER THE HEIGHT ARRAY (space separated)\n")
    heights = list(map(int, raw.split()))

    if not heights:
        raise ValueError("Array cannot be empty.")

    if len(heights) < 2:
        raise ValueError("Need at least 2 elements to form a container.")

    if any(h < 0 for h in heights):
        raise ValueError("Heights cannot be negative.")

    print(f"MAXIMUM WATER THE CONTAINER CAN HOLD: {max_water_container(heights)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
