"""
Grid and Square Visualizer

1. Solid Square 
2. Hollow Square 
3. Snake Number Grid 
4. Letter Square 
5. Sequential Letter Square 
"""

# -------- Basic Approach --------

def solid_square(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("*", end=" ")
        print()

def hollow_square(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print("  ", end="")
        print()

def snake_number_grid(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            k = (n * i) - (n - 1)
            for j in range(1, n + 1):
                print(f"{k:<4}", end="")
                k += 1
        else:
            k = (n * i)
            for j in range(1, n + 1):
                print(f"{k:<4}", end="")
                k -= 1
        print()

def letter_square(n):
    char = input("ENTER CHARACTER FOR SQUARE: ")
    for i in range(n):
        for j in range(n):
            print(char, end=" ")
        print()


def letter_square_sequential(n):
    """Prints A, B, C... in a square grid, wrapping at Z"""
    char_code = ord('A')
    for i in range(n):
        for j in range(n):
            print(chr(char_code), end=" ")
            char_code = ord('A') + (char_code - ord('A') + 1) % 26
        print()

# -------- Optimized Approach --------

def snake_grid_optimized(n):
    for i in range(n):
        row = list(range(i * n + 1, (i + 1) * n + 1))
        if i % 2 != 0: row = row[::-1]
        print("".join(f"{num:<4}" for num in row))

def hollow_square_optimized(n):
    if n <= 0: return
    print("* " * n)
    for _ in range(n - 2):
        print("* " + "  " * (n - 2) + "*")
    if n > 1: print("* " * n)

# -------- Main Execution --------

def main():
    try:
        print("--- GRID AND SQUARE VISUALIZER ---")
        print("1. Solid 2. Hollow 3. Snake 4. Letter 5. Sequential Letters")
        choice = int(input("SELECT: "))
        n = int(input("ENTER ROWS: "))
        
        if choice == 1: solid_square(n)
        elif choice == 2: hollow_square_optimized(n) 
        elif choice == 3: snake_grid_optimized(n)    
        elif choice == 4: letter_square(n)
        elif choice == 5: letter_square_sequential(n)
        else: print("INVALID CHOICE")
        
    except ValueError:
        print("INVALID INPUT")

if __name__ == "__main__":
    main()