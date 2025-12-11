nums = [7, 6, 5, 4, 3, 2, 1, 8]

l = 0 
x = 3 

window = nums[l:x]
res = []
res.append(min(window))

for r in range(x,len(nums)):
    window.remove(nums[l])
    l += 1 
    window.append(nums[r])
    res.append(min(window))

print((res))