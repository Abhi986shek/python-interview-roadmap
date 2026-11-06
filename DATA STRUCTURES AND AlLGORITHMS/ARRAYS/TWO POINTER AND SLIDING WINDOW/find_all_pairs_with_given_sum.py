"""
Find All Pairs Which Have the Given Sum

Print all unique pairs from the array that add up to the target sum.

Example:
Array: [1, 5, 3, 2, 4], Target: 6 -> Pairs: (1,5), (2,4)
"""

def find_pairs_with_sum(arr, target):
    arr = sorted(arr)

    left = 0
    right = len(arr) - 1
    pairs = []

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            pairs.append((arr[left], arr[right]))

            left += 1
            right -= 1

            # Skip duplicate elements
            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif total < target:
            left += 1

        else:
            right -= 1

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
