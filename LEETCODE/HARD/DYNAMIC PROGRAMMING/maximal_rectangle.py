"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
- rows == matrix.length
- cols == matrix[i].length
- 1 <= rows, cols <= 200
- matrix[i][j] is '0' or '1'.
"""

def maximal_rectangle(matrix):
    if not matrix:
        return 0
    
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
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0
    
    for i in range(rows):
        for j in range(cols):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
        max_area = max(max_area, largest_rectangle_area(heights[:]))
    
    return max_area


try:
    rows = int(input("ENTER ROWS\n"))
    cols = int(input("ENTER COLS\n"))
    matrix = []
    print("ENTER MATRIX (0 or 1):")
    for _ in range(rows):
        row = list(input().strip())
        matrix.append(row)
    print(f"MAXIMAL RECTANGLE: {maximal_rectangle(matrix)}")
except Exception as e:
    print(f"An error occurred: {e}")
