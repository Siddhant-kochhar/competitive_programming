

nums = [4,4,4,4,4,4] 
k = 4

n = len(nums)
curr_sum = 0 

prefix = [1] * n 

for i in range(n):
    if curr_sum <=k:
        curr_sum += nums[i] 
        print(curr_sum)
        prefix[i] = curr_sum
        print(prefix)
    else:
        prefix[i] = nums[i]
        curr_sum = 0 
        curr_sum = nums[i]
print(prefix.count(k))

