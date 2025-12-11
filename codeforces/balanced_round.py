'''
5 1
1 2 4 5 6
'''


diff = 1
x = [8, 3, 1, 4, 5, 10, 7, 3]

n = int(input())

for _ in range(n):
    m , diff = list(map(int, input().split()))
    x = list(map(int, input().split()))

    x.sort()   
    current = 1 
    longest = 1 

    for i in range(1,len(x)):
        if x[i] - x[i-1] <= diff:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    print(len(x)-longest)  
