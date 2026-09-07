from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0

        def get_sum(substr):
            nonlocal ans

            freq = Counter(substr)

            minimum = min(freq.values())
            maximum = max(freq.values())

            if maximum != minimum:
                ans += (maximum - minimum)

        def generate_substr(s):
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    substring = s[i:j]
                    get_sum(substring)

        generate_substr(s)

        return ans