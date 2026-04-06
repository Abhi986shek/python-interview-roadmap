"""
Fibonacci Series

A sequence where each number is the sum of the two preceding ones.

Example:
0, 1, 1, 2, 3, 5, 8...
"""

# -------- Basic Approach (All Use Cases) --------

def range_based():
    try:
        l = int(input("ENTER THE LOWER RANGE: "))
        u = int(input("ENTER THE UPPER RANGE: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    a, b = 0, 1
    print("\nTHE SERIES IS =>")

    while a <= u:
        if a >= l:
            print(a, end=" ")
        a, b = b, a + b


def limit_based():
    try:
        n = int(input("ENTER THE LIMIT OF THE SERIES: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    a, b = 0, 1
    print("\nTHE SERIES IS =>")

    while a <= n:
        print(a, end=" ")
        a, b = b, a + b


def term_based():
    try:
        n = int(input("ENTER NUMBER OF TERMS: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    a, b = 0, 1
    print("\nTHE SERIES IS =>")

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


def indexed_terms():
    try:
        n = int(input("ENTER NUMBER OF TERMS: "))
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
        return

    a, b = 0, 1
    print("\nFIBONACCI SERIES WITH TERM NUMBER:")

    for i in range(1, n + 1):
        if i <= 2:
            print(f"TERM NUMBER {i} = {i-1}")
        else:
            c = a + b
            print(f"TERM NUMBER {i} = {c}")
            a, b = b, c


def main():
    print("SELECT USE CASE:")
    print("1. RANGE BASED")
    print("2. LIMIT BASED")
    print("3. TERM BASED")
    print("4. TERM WITH INDEX")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID CHOICE")
        return

    if choice == 1:
        range_based()
    elif choice == 2:
        limit_based()
    elif choice == 3:
        term_based()
    elif choice == 4:
        indexed_terms()
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Single generator handles all cases
# - Avoids duplicate logic
# - Better modular design

def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def range_based(l, u):
    for num in fib_generator():
        if num > u:
            break
        if num >= l:
            print(num, end=" ")


def limit_based(n):
    for num in fib_generator():
        if num > n:
            break
        print(num, end=" ")


def term_based(n):
    gen = fib_generator()
    for _ in range(n):
        print(next(gen), end=" ")


def indexed_terms(n):
    gen = fib_generator()
    for i in range(1, n + 1):
        print(f"TERM NUMBER {i} = {next(gen)}")


def main():
    print("SELECT USE CASE:")
    print("1. RANGE BASED")
    print("2. LIMIT BASED")
    print("3. TERM BASED")
    print("4. TERM WITH INDEX")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("INVALID CHOICE")
        return

    if choice == 1:
        try:
            l = int(input("ENTER LOWER RANGE: "))
            u = int(input("ENTER UPPER RANGE: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        range_based(l, u)
    elif choice == 2:
        try:
            n = int(input("ENTER LIMIT: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        limit_based(n)
    elif choice == 3:
        try:
            n = int(input("ENTER NUMBER OF TERMS: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        term_based(n)
    elif choice == 4:
        try:
            n = int(input("ENTER NUMBER OF TERMS: "))
        except ValueError:
            print("INVALID INPUT! PLEASE ENTER A VALID INTEGER.")
            return
        indexed_terms(n)
    else:
        print("INVALID CHOICE")


if __name__ == "__main__":
    main()