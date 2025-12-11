class Solution:
    def stringStack(self, pat: str, tar: str) -> bool:
        i = len(pat) - 1
        j = len(tar) - 1
        if j > i:
            return False
        
        while i >= 0 and j >= 0:
            if pat[i] != tar[j]:
                i -= 2
            else:
                i -= 1
                j -= 1
        
        return j < 0