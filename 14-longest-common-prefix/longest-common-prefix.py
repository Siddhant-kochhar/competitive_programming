class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = sorted(strs)
        first = x[0]
        last = x[-1]

        ans = ""

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        return (ans)