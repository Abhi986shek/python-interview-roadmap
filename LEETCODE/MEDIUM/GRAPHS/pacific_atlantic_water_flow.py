"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[1]]
Output: [[0,0]]

Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5
"""

def pacific_atlantic(heights):
    if not heights:
        return []
    
    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    
    def dfs(i, j, visited):
        visited.add((i, j))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                dfs(ni, nj, visited)
    
    for i in range(m):
        dfs(i, 0, pacific)
        dfs(i, n - 1, atlantic)
    
    for j in range(n):
        dfs(0, j, pacific)
        dfs(m - 1, j, atlantic)
    
    return list(pacific & atlantic)


try:
    rows = int(input("ENTER ROWS\n"))
    cols = int(input("ENTER COLS\n"))
    heights = []
    print("ENTER HEIGHTS:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        heights.append(row)
    print(f"RESULT: {pacific_atlantic(heights)}")
except Exception as e:
    print(f"An error occurred: {e}")
