'''
2
5 10
3 5 3 2 1
4 6
10 8 6 4
'''


t = int(input())

for _ in range(t):
    p,m =  map(int, input().split())
    people = list(map(int, input().strip().split()))
    res = []

    for i in people:
        if m >= i:
            res.append("1")
            m -= i
        else:
            res.append("0")

print(int("".join(res)))
