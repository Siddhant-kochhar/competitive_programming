class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        one_positions = [i for i, num in enumerate(nums) if num == 1]
        #print(one_positions)
        res = True

        for i in range(1, len(one_positions)):
            if one_positions[i] - one_positions[i-1] - 1 < k:
                res = False
                break
        return(res)     