class Solution:
    def romanToInt(self, s: str) -> int:
        ref = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }


        ans = 0 

        for i in range(len(s)-1):
            if ref[s[i]] < ref[s[i+1]] and i != len(s)-1:
                ans -= ref[s[i]]
            else:
                ans += ref[s[i]]
        return (ans+ref[s[-1]])
