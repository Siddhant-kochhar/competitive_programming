class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0 

        prefix = [nums[0]]

        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])

        #print(prefix)

        left = 0 


        while left < len(prefix)-1:
            if prefix[left]%2 == (prefix[-1] - prefix[left])%2:
                count += 1 
            left += 1 
        return(count)   