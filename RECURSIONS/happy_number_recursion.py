"""
Happy Number (Recursion)

A number that eventually becomes 1 when replaced by the sum of the squares
of its digits repeatedly.

Example:
19 → 1² + 9² = 82 → ... → 1

Approach:
- Uses recursion to repeatedly sum squares of digits
- Detects cycle using known stopping condition (1 or 4)
"""


# -------- Basic Approach (Recursion) --------

def is_happy(n):
    # uses the known cycle detection trick — unhappy numbers always hit 4
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
            d = n % 10
            total += d * d
            n //= 10
        n = total
    return n == 1


def range_based(l, u):
    if l > u:
        return

    if is_happy(l):
        print(l)

    range_based(l + 1, u)


def highest_in_range(l, u):
    if u < l:
        return

    if is_happy(u):
        print("HIGHEST HAPPY NUMBER:", u)
        return

    highest_in_range(l, u - 1)


def second_highest_helper(l, u, count):
    if u < l:
        return

    if is_happy(u):
        count += 1
        if count == 2:
            print("SECOND HIGHEST HAPPY NUMBER:", u)
            return

    second_highest_helper(l, u - 1, count)


def second_highest_in_range(l, u):
    second_highest_helper(l, u, 0)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))

        if is_happy(n):
            print("ENTERED NUMBER IS A HAPPY NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A HAPPY NUMBER")

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
            print("HAPPY NUMBERS IN RANGE:")
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
# - Uses set to detect cycle
# - Cleaner and more reliable than using 4 trick

def is_happy_number(num: int) -> bool:
    seen = set()

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(d) ** 2 for d in str(num))

    return num == 1


def range_based(l, u):
    for i in range(l, u + 1):
        if is_happy_number(i):
            print(i)


def highest_in_range(l, u):
    for i in range(u, l - 1, -1):
        if is_happy_number(i):
            print("HIGHEST HAPPY NUMBER:", i)
            return


def second_highest_in_range(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_happy_number(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST HAPPY NUMBER:", i)
                return


def single_check(n):
    if is_happy_number(n):
        print("ENTERED NUMBER IS A HAPPY NUMBER")
    else:
        print("ENTERED NUMBER IS NOT A HAPPY NUMBER")


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