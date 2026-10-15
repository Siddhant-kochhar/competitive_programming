class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums)):
            #print(i)
            for j in range(i + 1, len(nums) + 1):
                #print(j)
                subarray = nums[i:j]
                total += len(set(subarray)) ** 2
                #print(subarray)
        return (total)
