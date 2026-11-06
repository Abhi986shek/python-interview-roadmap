"""
Check if a Pair with Given Sum Exists

Returns True if any two elements in the array add up to the target.

Example:
Array: [10, 15, 3, 7], Target: 17 -> True (10 + 7)
"""

def has_pair_with_sum(arr, target):
    arr = sorted(arr)

    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return True, (arr[left], arr[right])

        elif total < target:
            left += 1

        else:
            right -= 1

    return False, None



try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    target = int(input("ENTER THE TARGET SUM\n"))

    found, pair = has_pair_with_sum(arr, target)

    if found:
        print(f"YES, PAIR {pair} EXISTS WITH SUM {target}")
    else:
        print(f"NO PAIR EXISTS WITH SUM {target}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
