"""
Module: consecutive_occurrence_counter.py
Description: Compresses a string by replacing consecutive identical characters with
the character followed by its count. Example: "aaab" becomes "a3b".
Logic: Uses a sliding pointer to count consecutive matches, appending the character
and its count (if > 1) to build the compressed result.
"""
try:
    user_input = input("ENTER THE STRING\n")
    if not user_input:
        print("")
    else:
        result = ""
        i = 0
        while i < len(user_input):
            count = 1
            while i + 1 < len(user_input) and user_input[i] == user_input[i+1]:
                count += 1
                i += 1

            result += user_input[i]
            if count > 1:
                result += str(count)
            i += 1
        print(result)
except Exception as e:
    print(f"An error occurred: {e}")
