
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        n = len(nums)
        for i in nums:
            seen[i] += 1
        for key,value in seen.items():
            if value > n // 2:
                return key 
