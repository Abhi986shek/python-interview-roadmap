"""
Swaps two numbers without using a temporary variable.
Uses arithmetic addition/subtraction trick.
"""
def num_swap():
    try:
        a = input("ENTER THE VALUE OF A... ")
        b = input("ENTER THE VALUE OF B... ")

        # Validate input
        a = int(a)
        b = int(b)

        print("\n\nBEFORE SWAPPING =>")
        print("------------------")
        print("YOUR INSERTED VALUES ARE - ")
        print(f"A = {a} &")
        print(f"B = {b}")

        # Swap without temporary variable
        b = a + b
        a = b - a
        b = b - a

        print("\n\nAFTER SWAPPING =>")
        print("------------------")
        print("YOUR SWAPPED VALUES ARE - ")
        print(f"A = {a} &")
        print(f"B = {b}")

    except ValueError:
        print("Error: Please enter valid integers.")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    num_swap()
