"""
Find All Pairs Which Have the Given Sum

Print all unique pairs from the array that add up to the target sum.

Example:
Array: [1, 5, 3, 2, 4], Target: 6 -> Pairs: (1,5), (2,4)
"""

def find_pairs_with_sum(arr, target):
    seen = set()
    pairs = []
    visited = set()

    for num in arr:
        complement = target - num
        if complement in seen and (min(num, complement), max(num, complement)) not in visited:
            pairs.append((min(num, complement), max(num, complement)))
            visited.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return pairs


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    target = int(input("ENTER THE TARGET SUM\n"))

    pairs = find_pairs_with_sum(arr, target)

    if pairs:
        print(f"PAIRS WITH SUM {target}:")
        for a, b in pairs:
            print(f"  ({a}, {b})")
    else:
        print(f"NO PAIRS FOUND WITH SUM {target}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
