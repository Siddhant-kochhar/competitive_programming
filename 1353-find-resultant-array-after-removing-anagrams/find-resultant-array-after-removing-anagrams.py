from collections import Counter as counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]

        for i in range(1,len(words)):
            if (counter(words[i])) != (counter(words[i-1])):
                res.append(words[i])

        return (res)