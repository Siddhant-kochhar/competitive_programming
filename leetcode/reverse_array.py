x = [5,10,15,20,25]
res = [0] * len(x)

# i = 0 
# for j in range(len(x)-1,-1,-1):
#     res[i] = x[j]
#     i += 1
# print(res)

### Two pointer approach 

left = 0 
right = len(x) - 1 

while left <= right:
    x[left],x[right] = x[right],x[left]
    left += 1 
    right -= 1 

print(x)
