"""
Sum of Digits & Factorial (Recursion & Optimized)

Features:
1. SUM OF DIGITS
2. SUM OF DIGITS UNTIL SINGLE DIGIT
3. FACTORIAL

"""

# -------- Basic Recursive Approach --------

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def sum_until_single(n):
    if n == 0:
        return 0
    s = n % 10 + sum_until_single(n // 10)
    if s > 9:
        return sum_until_single(s)
    return s


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


# -------- Optimized Approach --------
# Improvements:
# - Uses string conversion for digits
# - Cleaner, more Pythonic
# - Avoids recursion for large ranges
# - Faster

def sum_of_digits_opt(n):
    return sum(int(d) for d in str(n))


def sum_until_single_opt(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


def factorial_opt(n):
    from math import prod
    return prod(range(1, n + 1)) if n > 0 else 1


# -------- Range & Highest Helpers --------

def range_based(func, l, u):
    for i in range(l, u + 1):
        print(f"{i} -> {func(i)}")


def highest_in_range(func, l, u):
    max_val = None
    max_num = None
    for i in range(l, u + 1):
        val = func(i)
        if max_val is None or val > max_val:
            max_val = val
            max_num = i
    print(f"HIGHEST RESULT: {func(max_num)} for NUMBER {max_num}")


def second_highest_in_range(func, l, u):
    results = [(i, func(i)) for i in range(l, u + 1)]
    results_sorted = sorted(results, key=lambda x: x[1], reverse=True)
    if len(results_sorted) < 2:
        print("SECOND HIGHEST RESULT NOT AVAILABLE")
    else:
        num, val = results_sorted[1]
        print(f"SECOND HIGHEST RESULT: {val} for NUMBER {num}")


# -------- Main Function --------

def main():
    try:
        print("SELECT OPERATION:")
        print("1. SUM OF DIGITS")
        print("2. SUM OF DIGITS UNTIL SINGLE DIGIT")
        print("3. FACTORIAL")

        operation = int(input("ENTER YOUR CHOICE: "))

        if operation not in [1, 2, 3]:
            print("INVALID OPERATION")
            return

        # Select function based on operation
        if operation == 1:
            func = sum_of_digits_opt
            name = "SUM OF DIGITS"
        elif operation == 2:
            func = sum_until_single_opt
            name = "SUM UNTIL SINGLE DIGIT"
        else:
            func = factorial_opt
            name = "FACTORIAL"

        print(f"SELECT USE CASE FOR {name}:")
        print("1. RANGE BASED")
        print("2. SINGLE CHECK")
        print("3. HIGHEST IN RANGE")
        print("4. SECOND HIGHEST IN RANGE")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice in [1, 3, 4]:
            l = int(input("ENTER LOWER LIMIT: "))
            u = int(input("ENTER UPPER LIMIT: "))

        if choice == 1:
            range_based(func, l, u)
        elif choice == 2:
            n = int(input("ENTER THE NUMBER: "))
            print(f"{func(n)}")
        elif choice == 3:
            highest_in_range(func, l, u)
        elif choice == 4:
            second_highest_in_range(func, l, u)
        else:
            print("INVALID CHOICE")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER VALID NUMBERS")


if __name__ == "__main__":
    main()