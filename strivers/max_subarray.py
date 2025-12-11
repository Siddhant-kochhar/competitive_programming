nums = [5,4,-1,7,8]
max_sum = float("-inf")

res = 0 
for i in range(len(nums)):
    if res < 0:
        res = 0 
    res += nums[i]
    max_sum = max(max_sum,res)

print(max_sum)