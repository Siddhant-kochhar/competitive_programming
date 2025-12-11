t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    ops = float('inf')
    for i in range(n - 1):
        if x[i] <= x[i + 1]:
            diff = x[i + 1] - x[i]
            res = diff // 2 + 1
            ops = min(ops, res)
        else:
            ops = 0
            break
    print(ops)
