"""
Happy Number

A number that eventually becomes 1 when replaced by the sum of the squares
of its digits repeatedly.

Example:
19 → 1² + 9² = 82 → ... → 1
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
        n = num

        while True:
            sum_val = 0

            while n > 0:
                d = n % 10
                sum_val += d * d
                n //= 10

            if sum_val == 1 or sum_val == 4:
                break

            n = sum_val

        if sum_val == 1:
            print(num)


def single_check():
    try:
        n = int(input("ENTER THE NUMBER: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    temp = n

    while True:
        sum_val = 0

        while temp > 0:
            d = temp % 10
            sum_val += d * d
            temp //= 10

        if sum_val == 1 or sum_val == 4:
            break

        temp = sum_val

    if sum_val == 1:
        print("ENTERED NUMBER IS A HAPPY NUMBER")
    else:
        print("ENTERED NUMBER IS NOT A HAPPY NUMBER")


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
# - Uses set to detect cycle
# - More robust than relying on fixed number (4)

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


def single_check(n):
    if is_happy_number(n):
        print("ENTERED NUMBER IS A HAPPY NUMBER")
    else:
        print("ENTERED NUMBER IS NOT A HAPPY NUMBER")


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