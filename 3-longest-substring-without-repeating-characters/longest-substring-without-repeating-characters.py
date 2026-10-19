class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0 

        n = len(s)
        seen = set()
        max_length = 0

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_length = max(max_length,r-l+1)
            r +=1 
        return (max_length)

