class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        arr.sort()
        n = len(arr)
        count = 0
        right = 1
        
        for left in range(n):
            if right <= left:
                right = left + 1
        
            while right < n and arr[right] - arr[left] < k:
                right += 1
        
            count += right - left - 1
        return count