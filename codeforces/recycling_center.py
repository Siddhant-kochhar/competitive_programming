import math

def calculate_deadlines(arr, c):
    deadlines = {}
    for a in arr:
        if a > c:
            # already greater than c, no free steps
            k = -1
        else:
            k = int(math.log2(c // a))  # floor(log2(c/a))
        deadlines[a] = k
    return deadlines


