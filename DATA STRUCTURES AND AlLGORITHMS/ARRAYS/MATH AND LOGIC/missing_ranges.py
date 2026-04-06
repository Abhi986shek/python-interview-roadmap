"""
Missing Ranges

Given a sorted array and a range [lower, upper], return all missing ranges.

Example:
Array: [0, 1, 3, 50, 75], lower = 0, upper = 99
Missing: ["2", "4->49", "51->74", "76->99"]
"""

def find_missing_ranges(arr, lower, upper):
    result = []
    prev = lower - 1

    for i in range(len(arr) + 1):
        curr = arr[i] if i < len(arr) else upper + 1

        if curr - prev >= 2:
            if curr - prev == 2:
                result.append(str(prev + 1))
            else:
                result.append(f"{prev + 1}->{curr - 1}")

        prev = curr

    return result


try:
    raw = input("ENTER THE SORTED ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    lower = int(input("ENTER THE LOWER BOUND\n"))
    upper = int(input("ENTER THE UPPER BOUND\n"))

    if lower > upper:
        raise ValueError("Lower bound must be less than or equal to upper bound.")

    result = find_missing_ranges(arr, lower, upper)

    if result:
        print(f"MISSING RANGES: {result}")
    else:
        print("NO MISSING RANGES")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
