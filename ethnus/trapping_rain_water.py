x = [4, 2, 9, 1, 0, 1, 1, 2]

n = len(x)
if n == 0:
    print(0)
else:
    left = [0] * n
    right = [0] * n

    left[0] = x[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], x[i])

    right[n - 1] = x[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], x[i])

    max_water = 0
    for i in range(n):
        max_water += min(left[i], right[i]) - x[i]

    print(max_water)