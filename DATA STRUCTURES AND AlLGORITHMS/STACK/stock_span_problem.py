"""
Stock Span Problem

For each day, find the number of consecutive days before it (including itself)
where the stock price was less than or equal to today's price.

Example:
Prices: [100, 80, 60, 70, 60, 75, 85]
Spans : [1,   1,  1,  2,  1,  4,  6]

Time Complexity  : O(n)
Space Complexity : O(n)
"""


def stock_span(prices):
    n = len(prices)
    spans = [1] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return spans


try:
    raw = input("ENTER THE STOCK PRICES (space separated)\n")
    prices = list(map(int, raw.split()))

    if not prices:
        raise ValueError("Prices cannot be empty.")

    if any(p < 0 for p in prices):
        raise ValueError("Stock prices cannot be negative.")

    spans = stock_span(prices)

    print("\nDAY  PRICE  SPAN")
    for i in range(len(prices)):
        print(f"  {i + 1}    {prices[i]}     {spans[i]}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
