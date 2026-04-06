"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Example 3:
Input: grid = [[0,2]]
Output: 0

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.
"""

from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    
    minutes = 0
    while queue:
        i, j, minutes = queue.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh -= 1
                queue.append((ni, nj, minutes + 1))
    
    return minutes if fresh == 0 else -1


try:
    rows = int(input("ENTER ROWS\n"))
    cols = int(input("ENTER COLS\n"))
    grid = []
    print("ENTER GRID (0=empty, 1=fresh, 2=rotten):")
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    print(f"MINUTES: {oranges_rotting(grid)}")
except Exception as e:
    print(f"An error occurred: {e}")
