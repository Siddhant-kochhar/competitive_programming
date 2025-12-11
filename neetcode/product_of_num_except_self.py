'''
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
'''

nums = [1,2,4,6]
n = len(nums)

prefix = [1] *n
postfix = [1] * n 

for i in range(1,n):
    prefix[i] = prefix[i-1]* nums[i-1]
print(prefix)

for i in range(n-2,-1,-1):
    postfix[i] = postfix[i+1] * nums[i+1]
print(postfix)

res = []

for i,j in zip(prefix,postfix):
    res.append(i*j)

print(res)