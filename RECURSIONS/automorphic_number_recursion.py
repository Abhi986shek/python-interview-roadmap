"""
Automorphic Number (Recursion)

A number whose square ends with the same digits as the number itself.

Example:
5 → 25
6 → 36
76 → 5776

Approach:
- Uses recursion to compare digits of number and its square
- Checks from last digit to first digit
"""


# -------- Basic Approach (Recursion) --------

def is_automorphic(n, m):
    if n == 0:
        return True

    if n % 10 != m % 10:
        return False

    return is_automorphic(n // 10, m // 10)


def range_based(l, u):
    if l > u:
        return

    if is_automorphic(l, l * l):
        print(l)

    range_based(l + 1, u)


def highest_in_range(l, u):
    if u < l:
        return

    if is_automorphic(u, u * u):
        print("HIGHEST AUTOMORPHIC NUMBER:", u)
        return

    highest_in_range(l, u - 1)


def second_highest_helper(l, u, count):
    if u < l:
        return

    if is_automorphic(u, u * u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST AUTOMORPHIC NUMBER:", u)
            return

    second_highest_helper(l, u - 1, count)


def second_highest_in_range(l, u):
    second_highest_helper(l, u, 0)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))

        if is_automorphic(n, n * n):
            print("ENTERED NUMBER IS AN AUTOMORPHIC NUMBER")
        else:
            print("ENTERED NUMBER IS NOT AN AUTOMORPHIC NUMBER")

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
# - Uses string comparison instead of recursion
# - Simpler and faster

def is_automorphic_opt(num: int) -> bool:
    square = str(num * num)
    return square.endswith(str(num))


def range_based(l, u):
    for i in range(l, u + 1):
        if is_automorphic_opt(i):
            print(i)


def highest_in_range(l, u):
    for i in range(u, l - 1, -1):
        if is_automorphic_opt(i):
            print("HIGHEST AUTOMORPHIC NUMBER:", i)
            return


def second_highest_in_range(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_automorphic_opt(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST AUTOMORPHIC NUMBER:", i)
                return


def single_check(n):
    if is_automorphic_opt(n):
        print("ENTERED NUMBER IS AN AUTOMORPHIC NUMBER")
    else:
        print("ENTERED NUMBER IS NOT AN AUTOMORPHIC NUMBER")


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