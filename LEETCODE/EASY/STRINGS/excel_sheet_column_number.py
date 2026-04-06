"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:
- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is in the range ["A", "FXSHRXW"].
"""


def title_to_number(column_title):
    result = 0
    for c in column_title:
        result = result * 26 + (ord(c) - ord('A') + 1)
    return result


try:
    column_title = input("ENTER COLUMN TITLE\n").upper()
    print(f"COLUMN NUMBER: {title_to_number(column_title)}")
except Exception as e:
    print(f"An error occurred: {e}")
