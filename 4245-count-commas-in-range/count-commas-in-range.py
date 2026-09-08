class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0 
        if n < 1000:
            return (0)
        else:
            ans += (n-1000)
        return ans+1