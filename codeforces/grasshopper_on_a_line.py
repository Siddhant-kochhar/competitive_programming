def helper(x, k):
    if x % k != 0:
        return (1, x)
    else:
        # Example split: 1 and x-1
        # Since x % k == 0, x-1 % k != 0 and 1 % k != 0
        return (2, 1, x - 1)

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    helper(x, k)
