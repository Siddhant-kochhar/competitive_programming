t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))

    if k in a:
        print("Yes")
    else:
        print("No")