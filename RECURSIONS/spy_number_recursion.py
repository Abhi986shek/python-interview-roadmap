"""
Spy Number (Recursion)

A Spy Number is a number where the sum of its digits
is equal to the product of its digits.

Example:
1124 → sum = 1+1+2+4 = 8
        product = 1*1*2*4 = 8

Approach:
- Uses recursion to process each digit
- Accumulates sum and product simultaneously
"""


# -------- Basic Approach (Recursion) --------

def spy(n, sum_val, prod):
    if n == 0:
        return sum_val == prod

    digit = n % 10
    return spy(n // 10, sum_val + digit, prod * digit)


def range_based(l, u):
    if l > u:
        return

    if spy(l, 0, 1):
        print(l)

    range_based(l + 1, u)


def highest_in_range(l, u):
    if u < l:
        return

    if spy(u, 0, 1):
        print("HIGHEST SPY NUMBER:", u)
        return

    highest_in_range(l, u - 1)


def second_highest_helper(l, u, count):
    if u < l:
        return

    if spy(u, 0, 1):
        count += 1
        if count == 2:
            print("SECOND HIGHEST SPY NUMBER:", u)
            return

    second_highest_helper(l, u - 1, count)


def second_highest_in_range(l, u):
    second_highest_helper(l, u, 0)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))

        if spy(n, 0, 1):
            print("ENTERED NUMBER IS A SPY NUMBER")
        else:
            print("ENTERED NUMBER IS NOT A SPY NUMBER")

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

def is_spy_number(num: int) -> bool:

    def helper(n):
        if n == 0:
            return (0, 1)

        s, p = helper(n // 10)
        digit = n % 10
        return (s + digit, p * digit)

    sum_val, prod = helper(num)
    return sum_val == prod


def range_based(l, u):
    for i in range(l, u + 1):
        if is_spy_number(i):
            print(i)


def highest_in_range(l, u):
    for i in range(u, l - 1, -1):
        if is_spy_number(i):
            print("HIGHEST SPY NUMBER:", i)
            return


def second_highest_in_range(l, u):
    count = 0
    for i in range(u, l - 1, -1):
        if is_spy_number(i):
            count += 1
            if count == 2:
                print("SECOND HIGHEST SPY NUMBER:", i)
                return


def single_check(n):
    if is_spy_number(n):
        print("ENTERED NUMBER IS A SPY NUMBER")
    else:
        print("ENTERED NUMBER IS NOT A SPY NUMBER")


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