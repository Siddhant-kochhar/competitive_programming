class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_element = min(nums)
        max_element = max(nums)

        missing_element = []

        for i in range(min_element, max_element + 1):
            if i not in nums:
                missing_element.append(i)

        return (missing_element)