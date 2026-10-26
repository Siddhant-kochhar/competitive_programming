
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:

        def at_most_k(nums, k):
            left = 0
            count = 0
            odds = 0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    odds += 1

                while odds > k:
                    if nums[left] % 2 != 0:
                        odds -= 1
                    left += 1

                count += right - left + 1

            return count

        return at_most_k(nums, k) - at_most_k(nums, k - 1)
