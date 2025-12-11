n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x_set = set()
for ai, bi in zip(a, b):
    if bi != -1:
        x_set.add(ai + bi)

if len(x_set) > 1:
    print(0)
else:
    x = x_set.pop() if x_set else None
    if x is None:
        # All b_i are -1
        x_min = max(a)
        x_max = min(a) + k
        print(x_max - x_min + 1)
    else:
        for ai, bi in zip(a, b):
            if bi == -1:
                if not (0 <= x - ai <= k):
                    print(0)
                    break
        else:
            print(1)
