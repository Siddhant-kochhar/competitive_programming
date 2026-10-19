class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = {}

        for i,j in enumerate(nums):
            #print(i,j)
            if j in res:
                res[j].append(i)
            else:
                res[j] = [i]
        if target in res:
            return res[target]
        else:
            return []