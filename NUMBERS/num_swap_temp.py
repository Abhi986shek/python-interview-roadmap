"""
Swaps two numbers using a temporary variable.
"""
def num_swapping():
    try:
        a = input("ENTER THE VALUE OF A .. ")
        b = input("ENTER THE VALUE OF B .. ")

        # Validate input
        a = int(a)
        b = int(b)

        print("BEFORE SWAPPING =>")
        print("-------------------")
        print("YOUR INSERTED VALUES ARE..")
        print(f"A = {a} &")
        print(f"B = {b}")

        # Swap using a temporary variable
        c = b
        b = a
        a = c

        print("\nAFTER SWAPPING =>")
        print("-------------------")
        print("YOUR SWAPPED VALUES ARE..")
        print(f"A = {a} &")
        print(f"B = {b}")

    except ValueError:
        print("Error: Please enter valid integers.")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    num_swapping()