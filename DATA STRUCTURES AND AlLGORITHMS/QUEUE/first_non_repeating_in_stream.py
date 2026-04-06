"""
First Non-Repeating Character in a Stream

For each character read from a stream, print the first non-repeating character
seen so far. If all characters repeat, print -1.

Example:
Stream : a a b c
Output : a -1 b b

Time Complexity  : O(n)
Space Complexity : O(n)
"""

from collections import deque, Counter


def first_non_repeating_stream(stream):
    freq = {}
    dq = deque()
    result = []

    for char in stream:
        freq[char] = freq.get(char, 0) + 1
        dq.append(char)

        # remove characters from front that are now repeating
        while dq and freq[dq[0]] > 1:
            dq.popleft()

        result.append(dq[0] if dq else -1)

    return result


try:
    stream = input("ENTER THE STREAM OF CHARACTERS (space separated)\n").split()

    if not stream:
        raise ValueError("Stream cannot be empty.")

    result = first_non_repeating_stream(stream)

    print("\nCHAR  ->  FIRST NON-REPEATING SO FAR")
    for i in range(len(stream)):
        print(f"  {stream[i]}   ->   {result[i]}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
