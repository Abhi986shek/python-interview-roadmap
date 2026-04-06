"""
Neon Number (Recursion)

A number where the sum of digits of its square
is equal to the number itself.

Example:
9 → 9² = 81 → 8 + 1 = 9

Approach:
- Uses recursion to sum digits of square
- Compares sum with original number
"""


# -------- Basic Approach (Recursion) --------

def is_neon(n, sum_val, m):
    if m == 0:
        return n == sum_val

    sum_val += m % 10
    return is_neon(n, sum_val, m // 10)


def range_based(l, u):
    if l > u:
        return

    if is_neon(l, 0, l * l):
        print(l)

    range_based(l + 1, u)


def highest_in_range(l, u):
    if u < l:
        return

    if is_neon(u, 0, u * u):
        print("HIGHEST NEON NUMBER:", u)
        return

    highest_in_range(l, u - 1)


def second_highest_helper(l, u, count):
    if u < l:
        return

    if is_neon(u, 0, u * u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST NEON NUMBER:", u)
            return

    second_highest_helper(l, u - 1, count)


def second_highest_in_range(l, u):
    second_highest_helper(l, u, 0)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))

        if is_neon(n, 0, n * n):
            print("ENTERED NUMBER IS A NEON NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A NEON NUMBER")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID NUMBER")


def main():
    try:
        print("SELECT USE CASE:")
        print("1. RANGE BASED")
        print("2. SINGLE CHECK")
        print("3. HIGHEST IN RANGE")
        print("4. SECOND HIGHEST IN RANGE")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            range_based(l, u)

        elif choice == 2:
            single_check()

        elif choice == 3:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            highest_in_range(l, u)

        elif choice == 4:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            second_highest_in_range(l, u)

        else:
            print("INVALID CHOICE")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER NUMBERS ONLY")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Uses direct sum with string conversion
# - Faster and cleaner

def is_neon_opt(num: int) -> bool:
    return sum(int(d) for d in str(num * num)) == num


def range_based(l, u):
    for i in range(l, u + 1):
        if is_neon_opt(i):
            print(i)


def highest_in_range(l, u):
    for i in range(u, l - 1, -1):
        if is_neon_opt(i):
            print("HIGHEST NEON NUMBER:", i)
            return


def second_highest_in_range(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_neon_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST NEON NUMBER:", i)
                return


def single_check(n):
    if is_neon_opt(n):
        print("ENTERED NUMBER IS A NEON NUMBER")
    else:
        print("ENTERED NUMBER IS NOT A NEON NUMBER")


def main():
    try:
        print("SELECT USE CASE:")
        print("1. RANGE BASED")
        print("2. SINGLE CHECK")
        print("3. HIGHEST IN RANGE")
        print("4. SECOND HIGHEST IN RANGE")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            range_based(l, u)

        elif choice == 2:
            n = int(input("ENTER NUMBER: "))
            single_check(n)

        elif choice == 3:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            highest_in_range(l, u)

        elif choice == 4:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
            second_highest_in_range(l, u)

        else:
            print("INVALID CHOICE")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER VALID NUMBERS")


if __name__ == "__main__":
    main()