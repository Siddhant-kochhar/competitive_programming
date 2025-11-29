from collections import Counter 

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        seen = Counter(s)
        if letter not in seen.keys():
            return 0 
        else:
            return ((seen[letter] * 100) // n)