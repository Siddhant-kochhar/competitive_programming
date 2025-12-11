'''
5
100 50 200 150 200
'''

n = int(input())
a = list(map(int, input().split()))

if len(a) == 1:
    print(0)
else:
    amazing = 0
    min_p = a[0]
    max_p = a[0]
    for i in range(1, n):
        current = a[i]
        is_amazing = False
        if current > max_p:
            max_p = current
            is_amazing = True
        elif current < min_p:
            min_p = current
            is_amazing = True
        if is_amazing:
            amazing += 1
    print(amazing)
