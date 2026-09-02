class Solution:
    def reverseWords(self, s: str) -> str:

        s_split = s.split()
        res = []
        for i in range(len(s_split)-1,-1,-1):
            if i != " ":
                res.append(s_split[i])
        return " ".join(res)