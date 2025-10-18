class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        used = defaultdict(bool)
        max_used = float('-inf')

        for num in nums:
            start = num - k 
            end = num + k 

            candidate = max(start,max_used + 1)

            while candidate <= end:
                if not used[candidate]:
                    used[candidate] = True
                    max_used = candidate 
                    break
                candidate +=1 
        return sum(used.values())
