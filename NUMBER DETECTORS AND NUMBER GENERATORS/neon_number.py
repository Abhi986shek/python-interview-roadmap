"""
Neon Number

A number where the sum of digits of its square is equal to the number itself.

Example:
9 → 9² = 81 → 8 + 1 = 9
"""

# -------- Basic Approach --------

def range_based():
    try:
        l = int(input("ENTER THE LOWER LIMIT: "))
        u = int(input("ENTER THE UPPER LIMIT: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    for num in range(l, u + 1):
        square = num * num
        sum_val = 0

        while square > 0:
            sum_val += square % 10
            square //= 10

        if sum_val == num:
            print(num)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    square = n * n
    sum_val = 0

    while square > 0:
        sum_val += square % 10
        square //= 10

    print("SUM OF DIGITS OF SQUARE =", sum_val)

    if sum_val == n:
        print(f"{n} IS A NEON NUMBER")
    else:
        print(f"{n} IS NOT A NEON NUMBER")


def main():
    print("SELECT USE CASE:")
    print("2. SINGLE NUMBER CHECK")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID CHOICE")
        return

    if choice == 1:
        range_based()
    elif choice == 2:
        single_check()
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Uses string-based digit sum
# - Cleaner and more Pythonic

def is_neon_number(num: int) -> bool:
    square = num * num
    return sum(int(d) for d in str(square)) == num


def range_based(l, u):
    for i in range(l, u + 1):
        if is_neon_number(i):
            print(i)


def single_check(n):
    square = n * n
    sum_val = sum(int(d) for d in str(square))

    print("SUM OF DIGITS OF SQUARE =", sum_val)

    if is_neon_number(n):
        print(f"{n} IS A NEON NUMBER")
    else:
        print(f"{n} IS NOT A NEON NUMBER")


def main():
    print("SELECT USE CASE:")
    print("1. RANGE BASED")
    print("2. SINGLE NUMBER CHECK")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID CHOICE")
        return

    if choice == 1:
        try:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        range_based(l, u)
    elif choice == 2:
        try:
            n = int(input("ENTER NUMBER: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        single_check(n)
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()