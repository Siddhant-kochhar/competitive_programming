n,m = list(map(int, input().split()))

next_buying_day = m 

current_day = 0

while n >0:
    current_day +=1
    n -= 1 
    if current_day == next_buying_day:
        n += 1
        next_buying_day += m
    else:
        continue

print(current_day)