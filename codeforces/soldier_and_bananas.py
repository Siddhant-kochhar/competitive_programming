k , n , w = map(int, input().split())

i = 1 
while w > 0 :
    n -= k*i 
    i += 1
    w -= 1
if n < 0:
    print(-n)
else:
    print(0)
    
