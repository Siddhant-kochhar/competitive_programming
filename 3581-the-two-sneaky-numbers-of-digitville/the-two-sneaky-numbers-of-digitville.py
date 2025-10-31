class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter

        nums_dict = Counter(nums)
        res = []
        for key,value in nums_dict.items():
            if value == 2:
                res.append(key)
        return res