class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        current_length = 1
        present_length = 0
        res = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
            else:
                present_length = current_length
                current_length = 1

            res = max(res, max(current_length // 2, min(present_length, current_length)))

            if res >= k:
                return True

        return False
