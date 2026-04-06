"""
Unique Triplets with Sum Zero

Find all unique triplets in the array that add up to zero.

Example:
Array: [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]]
"""

def three_sum_zero(arr):
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        # skip duplicates for the first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


try:
    raw = input("ENTER THE ARRAY ELEMENTS (space separated)\n")
    arr = list(map(int, raw.split()))

    if len(arr) < 3:
        raise ValueError("Array must have at least 3 elements.")

    result = three_sum_zero(arr)

    if result:
        print("TRIPLETS WITH SUM ZERO:")
        for triplet in result:
            print(f"  {triplet}")
    else:
        print("NO TRIPLETS FOUND WITH SUM ZERO")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
