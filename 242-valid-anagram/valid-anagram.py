class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = list(s)
        two = list(t)

        return sorted(one) == sorted(two)