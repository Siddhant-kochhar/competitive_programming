class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        def find_max(nums,i):
            return max(nums[:i+1])

        def find_min(nums,j):
            return min(nums[j::])

        for i in range(len(nums)):
            x = find_max(nums,i) - find_min(nums,i) 
            #print(find_max(nums,i) )
            #print(find_min(nums,i))
            if x<=k:
                return (i)
            else:
                continue
        return (-1)