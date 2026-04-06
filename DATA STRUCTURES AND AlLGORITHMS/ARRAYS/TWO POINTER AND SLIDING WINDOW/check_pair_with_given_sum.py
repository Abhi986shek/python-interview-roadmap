"""
Check if a Pair with Given Sum Exists

Returns True if any two elements in the array add up to the target.

Example:
Array: [10, 15, 3, 7], Target: 17 -> True (10 + 7)
"""

def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True, (target - num, num)
        seen.add(num)
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
