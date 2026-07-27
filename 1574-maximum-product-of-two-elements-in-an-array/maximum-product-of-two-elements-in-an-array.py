class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dup = [-i for i in nums]
        heapq.heapify(dup)
        a = -heapq.heappop(dup)
        b = -heapq.heappop(dup)
        return (a-1)*(b-1)
