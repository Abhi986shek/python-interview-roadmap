"""
Armstrong Number

A number equal to the sum of its digits raised to the power of the number of digits.

Example:
153 → 1³ + 5³ + 3³ = 153
"""

# -------- Basic Approach --------

def range_based():
    try:
        l = int(input("ENTER THE LOWER LIMIT: "))
        u = int(input("ENTER THE UPPER LIMIT: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    for i in range(l, u + 1):
        temp1 = i
        temp2 = i

        sum_val = 0
        itr = 0

        # COUNT DIGITS
        while temp1 > 0:
            itr += 1
            temp1 //= 10

        # CALCULATE POWER SUM
        while temp2 > 0:
            d = temp2 % 10
            prod = 1

            for _ in range(itr):
                prod *= d

            sum_val += prod
            temp2 //= 10

        if sum_val == i:
            print(i)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    sum_val = 0
    temp = n
    l = n

    # COUNT DIGITS
    itr = 0
    while l > 0:
        itr += 1
        l //= 10

    print("\nTHE NUMBER OF DIGITS IS =", itr)

    # CALCULATION
    while temp > 0:
        d = temp % 10
        prod = 1

        for _ in range(itr):
            prod *= d

        sum_val += prod
        temp //= 10

    print(f"\nSUM OF DIGITS RAISED TO POWER {itr} = {sum_val}")

    if n == sum_val:
        print("\nENTERED NUMBER IS AN ARMSTRONG NUMBER")
    else:
        print("\nENTERED NUMBER IS NOT AN ARMSTRONG NUMBER")


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
        range_based()
    elif choice == 2:
        single_check()
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Uses string conversion for digit count
# - Uses power operator instead of loop
# - Cleaner and faster

def is_armstrong(num: int):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num, power, total


def range_based(l, u):
    for i in range(l, u + 1):
        result, _, _ = is_armstrong(i)
        if result:
            print(i)


def single_check(n):
    result, power, total = is_armstrong(n)

    print("\nTHE NUMBER OF DIGITS IS =", power)
    print(f"SUM OF DIGITS RAISED TO POWER {power} = {total}")

    if result:
        print("\nENTERED NUMBER IS AN ARMSTRONG NUMBER")
    else:
        print("\nENTERED NUMBER IS NOT AN ARMSTRONG NUMBER")


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