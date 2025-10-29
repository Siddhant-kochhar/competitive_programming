class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")

        res = 0 
        for i in range(len(nums)):
            if res < 0:
                res = 0 
            res += nums[i]
            max_sum = max(max_sum,res)

        return (max_sum)