"""
Returns the number of days in a given month, accounting for leap years.
"""
def days_in_month():
    try:
        y = input("ENTER THE YEAR NUMBER... ")
        m = input("ENTER THE MONTH NUMBER (HAS TO BE AMONG 1-12): ")

        # Validate input
        y = int(y)
        m = int(m)

        if m in [1, 3, 5, 7, 8, 10, 12]:
            print("31 DAYS ARE THERE IN THIS MONTH")
        elif m in [4, 6, 9, 11]:
            print("30 DAYS ARE THERE IN THIS MONTH")
        elif m == 2:
            # Leap year check
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                print("29 DAYS ARE THERE IN THIS MONTH")
            else:
                print("28 DAYS ARE THERE IN THIS MONTH")
        else:
            print("INVALID CHOICE !!! :(")

    except ValueError:
        print("Error: Please enter valid integers for year and month.")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    days_in_month()