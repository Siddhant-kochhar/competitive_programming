class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums_idx = {}
        for i,j in enumerate(nums1):
            nums_idx[j] = i 
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums_idx[val]
                res[idx] = curr
            if curr in nums_idx:
                stack.append(curr)
        return res
