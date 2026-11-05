"""
Module: character_occurrence_tagger.py
Description: Tags each character with its occurrence number for repeated instances.
Logic: Iterates through the character list; when a character repeats, replaces
subsequent occurrences with their count index (e.g., "aab" -> "a1a2b").
"""
try:
    s = list(input("ENTER THE STRING\n"))

    for i in range(len(s)):
        count = 1

        if '0' <= s[i] <= '9':
            continue

        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                count += 1
                s[j] = '0'  # Mark as processed

        s[i] = s[i] + str(count)

    print("".join(s))

except Exception as e:
    print(f"Error: {e}")
