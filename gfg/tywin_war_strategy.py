arr = [5, 6, 3, 2, 1]
k = 2

lucky_count = 0
costs = []

for num in arr:
    if num % k == 0:
        lucky_count += 1
    else:
       
        cost = k - (num % k)
        costs.append(cost)


required_lucky = (len(arr) + 1) // 2  

if lucky_count >= required_lucky:
    print(0)  
else:
   
    costs.sort()
    needed = required_lucky - lucky_count
    total_cost = sum(costs[:needed])
    print(total_cost)
