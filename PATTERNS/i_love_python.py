"""
I LOVE PYTHON Pattern Generator
Consolidates individual letter logic into a single message.
"""

def print_I(n):
    for i in range(1, n + 1):
        for j in range(1, n):
            if i == 1 or i == n or j == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_L(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == n or j == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_O(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_V(n):
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if i == j or i + j == 2 * n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_E(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or i == n // 2 + 1 or j == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_P(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1 or (i == 1 or i == n // 2 + 1) and j < n or (j == n and i > 1 and i < n // 2 + 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_Y(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i == j or i + j == n + 1) and i <= n // 2 + 1 or (j == n // 2 + 1 and i > n // 2 + 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_T(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == n // 2 + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_H(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1 or j == n or i == n // 2 + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_N(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == 1 or j == n or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_heart():
    for i in range(6):
        for j in range(7):
            if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def main():
    try:
        n = int(input("ENTER THE NUMBER OF ROWS FOR LETTERS: "))
        if n < 3:
            print("Please enter a number 3 or higher for better visibility.")
            return

        print("\n--- I ---")
        print_I(n)
        
        print("\n--- LOVE ---")
        print_L(n)
        print()
        print_O(n)
        print()
        print_V(n)
        print()
        print_E(n)

        print("\n--- PYTHON ---")
        print_P(n)
        print()
        print_Y(n)
        print()
        print_T(n)
        print()
        print_H(n)
        print()
        print_O(n)
        print()
        print_N(n)

        print("\n--- AND FINALLY ---")
        print_heart()

    except ValueError:
        print("INVALID INPUT! Please enter a valid integer.")

if __name__ == "__main__":
    main()