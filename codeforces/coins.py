t = int(input())
for _ in range(t):
    n , k = map(int,input().split())

    if n %2 ==0 or (n-k)%2 ==0:
        print("Yes")
    else:
        print("No")