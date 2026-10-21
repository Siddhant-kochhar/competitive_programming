class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0 
        zeros = 0 
        max_length = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] ==0:
                    zeros -=1 
                left += 1
            max_length = max(max_length,r-left+1)
        return (max_length)