"""
Finding the Majority Element (Boyer-Moore Voting Algorithm)

A majority element appears more than n/2 times in the array.
Returns the element if it exists, otherwise reports none found.

Example:
Array: [3, 2, 3] -> Majority: 3
"""

def find_majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # verify the candidate is actually a majority
    if arr.count(candidate) > len(arr) // 2:
        return candidate

    return None


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if not arr:
        raise ValueError("Array cannot be empty.")

    result = find_majority_element(arr)

    if result is not None:
        print(f"MAJORITY ELEMENT: {result}")
    else:
        print("NO MAJORITY ELEMENT EXISTS")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
