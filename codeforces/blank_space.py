t = int(input())
for _ in range(t):
    size = int(input())
    x = list(map(int,input().split()))

    res = float('-inf')   # Initialize to track the maximum length of consecutive zeros
    len_largest = 0       # To count current streak of consecutive zeros

    for j in range(len(x)):
        if x[j] == 0:
            len_largest += 1              # Extend current zero streak
        else:
            res = max(res, len_largest)  # Update maximum if this streak is larger
            len_largest = 0              # Reset current streak on seeing 1

    # Final update after loop to handle trailing zeros
    res = max(res, len_largest)

    print(res)  # Output: 2 for this example
