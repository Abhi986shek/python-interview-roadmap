"""
Decimal ↔ Binary Conversion (Recursion)

Converts numbers between decimal and binary using recursion.

Example:
Decimal → Binary:
5 → 101

Binary → Decimal:
101 → 5

Approach:
- Uses recursion to process digits
- Builds result using positional values (base 2)
"""


# -------- Basic Approach (Recursion) --------

def decimal_to_binary(n, bin_val, i):
    if n == 0:
        return bin_val

    bin_val = (n % 2) * i + bin_val
    return decimal_to_binary(n // 2, bin_val, i * 10)


def binary_to_decimal(n, deci, i):
    if n == 0:
        return deci

    deci = (n % 10) * i + deci
    return binary_to_decimal(n // 10, deci, i * 2)


def main():
    try:
        print("SELECT OPERATION:")
        print("1. DECIMAL TO BINARY")
        print("2. BINARY TO DECIMAL")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            n = int(input("ENTER DECIMAL NUMBER: "))
            result = decimal_to_binary(n, 0, 1)
            print("BINARY VALUE:", result)

        elif choice == 2:
            n = int(input("ENTER BINARY NUMBER: "))
            result = binary_to_decimal(n, 0, 1)
            print("DECIMAL VALUE:", result)

        else:
            print("INVALID CHOICE")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER NUMBERS ONLY")


if __name__ == "__main__":
    main()


# -------- Optimized Approach --------
# Improvements:
# - Uses built-in conversions
# - More efficient and reliable

def decimal_to_binary_opt(n: int) -> str:
    return bin(n)[2:]


def binary_to_decimal_opt(n: str) -> int:
    return int(n, 2)


def main():
    try:
        print("SELECT OPERATION:")
        print("1. DECIMAL TO BINARY")
        print("2. BINARY TO DECIMAL")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            n = int(input("ENTER DECIMAL NUMBER: "))
            print("BINARY VALUE:", decimal_to_binary_opt(n))

        elif choice == 2:
            n = input("ENTER BINARY NUMBER: ")
            print("DECIMAL VALUE:", binary_to_decimal_opt(n))

        else:
            print("INVALID CHOICE")

    except ValueError:
        print("INVALID INPUT! PLEASE ENTER VALID NUMBERS")


if __name__ == "__main__":
    main()