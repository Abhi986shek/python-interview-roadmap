"""
Trapping Rain Water

Given an elevation map, calculate how much water can be trapped after raining.

Example:
Heights: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> Water Trapped: 6
"""

def trap_rain_water(heights):
    if not heights:
        return 0

    left, right = 0, len(heights) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1

    return water


try:
    raw = input("ENTER THE ELEVATION MAP (space separated)\n")
    heights = list(map(int, raw.split()))

    if not heights:
        raise ValueError("Array cannot be empty.")

    if any(h < 0 for h in heights):
        raise ValueError("Heights cannot be negative.")

    print(f"TOTAL WATER TRAPPED: {trap_rain_water(heights)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
