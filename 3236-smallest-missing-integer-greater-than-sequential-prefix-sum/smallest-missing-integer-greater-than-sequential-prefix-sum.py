class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        current = nums[0]

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                current += nums[i]
            else:
                break

        for i in range(current, current + 50):  # Adjust the range as needed
            if i not in nums:
                return (i)
                break
