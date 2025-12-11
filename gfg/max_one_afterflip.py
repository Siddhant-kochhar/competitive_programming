x = [1, 0, 0, 1, 0, 1, 0, 1]
k = 2

left = 0 
zeros = 0 

res = float("-inf")

for right in range(len(x)):
    if x[right] == 0:
        zeros +=1 
    
    while zeros > k:
        if x[left] == 0:
            zeros -= 1
        left += 1
    
    res = max(res,right - left + 1)

print(res)

