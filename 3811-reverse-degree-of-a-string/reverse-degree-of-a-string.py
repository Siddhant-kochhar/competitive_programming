class Solution:
    def reverseDegree(self, s: str) -> int:
        ans =0
        for i,j in enumerate(s):
            #print(i,j)

            ans += (((ord('z') - ord(j) + 1)) * (i + 1))
            

        return (ans)

