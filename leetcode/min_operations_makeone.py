'''
Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].

Hint 1
Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.
Hint 2
Try finding the shortest subarray with a gcd equal to 1.
'''

from math import gcd 

nums = [2,6,3,4]
n = len(nums)

if 1 in nums:
    print(n - nums.count(1))
else:
    min_len = float('inf')
    for i in range(n):
        curr_gcd = nums[i]
        for j in range(i+1,n):
            curr_gcd = gcd(curr_gcd, nums[j])
            if curr_gcd == 1:
                min_len = min(min_len, j - i + 1)
                break
    if min_len == float('inf'):
        print(-1)
    else:
        print(n -1 + min_len -1)


