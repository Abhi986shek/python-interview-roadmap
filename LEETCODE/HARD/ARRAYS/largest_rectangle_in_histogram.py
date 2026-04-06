"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    heights.pop()
    return max_area


try:
    heights = list(map(int, input("ENTER HEIGHTS (space separated)\n").split()))
    print(f"LARGEST RECTANGLE AREA: {largest_rectangle_area(heights)}")
except Exception as e:
    print(f"An error occurred: {e}")
