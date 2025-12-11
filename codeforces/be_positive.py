'''
3
3
-1 0 1
4
-1 -1 0 1
5
-1 -1 -1 0 0
'''

from collections import Counter

n = int(input())
for _ in range(n):
    m = int(input())
    x = list(map(int, input().split()))
    x_dict = Counter(x)
    print(x_dict)

    res = 0
    for key, value in x_dict.items():
        if key == -1:
            if value % 2 == 0:
                res += 0
            else:
                x = value % 2
                res += x * 2

        elif key == 0:
            res += value
        else:
            continue

    print(res)
