class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == len(goal):
            new_str = s+s
            if goal in new_str:
                return True
            return False
        return False