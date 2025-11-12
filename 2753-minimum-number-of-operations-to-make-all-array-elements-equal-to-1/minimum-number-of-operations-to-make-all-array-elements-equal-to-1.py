from math import gcd 

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)

        if 1 in nums:
            return (n - nums.count(1))
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
                return (-1)
            else:
                return (n -1 + min_len -1)