class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr = 0

        for i in s:
            if i == "(":
                curr += 1 
            elif i == ")":
                max_depth = max(max_depth,curr)
                curr -=1 
            else:
                continue

        return(max_depth)