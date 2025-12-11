t = int(input())
for _ in range(t):
    size = int(input())
    x = list(map(int,input().split()))

    operation = 0

    for i in range(1,len(x)):
        if x[i]%2 == x[i-1]%2:
            operation += 1 

    print(operation)