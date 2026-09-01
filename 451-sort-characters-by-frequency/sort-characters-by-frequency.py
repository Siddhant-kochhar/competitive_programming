from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = ""

        for char,count in sorted_freq:
            ans += char * count

        return (ans)