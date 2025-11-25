class Solution:
    def subarrayXor(self, arr):
        ans = 0
        n = len(arr)
        for i in range(n):
            times = (i + 1) * (n - i)
            if times % 2 != 0:   
                ans ^= arr[i]
        return ans
