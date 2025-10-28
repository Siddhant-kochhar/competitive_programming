class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        length = 0
        words_set = [set(words[i]) for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if not (words_set[i] & words_set[j]):
                    length = max(length, len(words[i]) * len(words[j]))
        return length