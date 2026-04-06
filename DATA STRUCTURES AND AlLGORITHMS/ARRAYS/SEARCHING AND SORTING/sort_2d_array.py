"""
Sort a 2D Array Row-wise

Sorts each row of a 2D matrix in ascending order.

Example:
Input:  [[3,1,2],[9,5,7],[4,6,8]]
Output: [[1,2,3],[5,7,9],[4,6,8]]
"""

def sort_2d_array(matrix):
    for row in matrix:
        row.sort()
    return matrix


try:
    rows = int(input("ENTER NUMBER OF ROWS\n"))
    cols = int(input("ENTER NUMBER OF COLUMNS\n"))

    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be greater than 0.")

    matrix = []
    for i in range(rows):
        raw = input(f"ENTER ROW {i + 1} ELEMENTS (space separated)\n")
        row = list(map(int, raw.split()))
        if len(row) != cols:
            raise ValueError(f"Row {i + 1} must have exactly {cols} elements.")
        matrix.append(row)

    result = sort_2d_array(matrix)

    print("SORTED 2D ARRAY:")
    for row in result:
        print(row)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
