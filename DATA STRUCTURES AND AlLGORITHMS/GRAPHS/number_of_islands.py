"""
Number of Islands

Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and formed by connecting adjacent land cells
horizontally or vertically.
Uses BFS to sink each island once found.

Example:
Grid:
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
Answer: 3

Time Complexity  : O(m * n)  - m = rows, n = cols
Space Complexity : O(m * n)  - BFS queue in worst case
"""

from collections import deque


def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # mark as visited by sinking it

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                count += 1

    return count


try:
    rows = int(input("ENTER NUMBER OF ROWS: "))
    cols = int(input("ENTER NUMBER OF COLUMNS: "))

    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be greater than 0.")

    grid = []
    for i in range(rows):
        row = input(f"ENTER ROW {i + 1} (space separated 0s and 1s): ").split()
        if len(row) != cols:
            raise ValueError(f"Row {i + 1} must have exactly {cols} elements.")
        if any(c not in ('0', '1') for c in row):
            raise ValueError("Grid must contain only 0s and 1s.")
        grid.append(row)

    print(f"NUMBER OF ISLANDS: {num_islands(grid)}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
