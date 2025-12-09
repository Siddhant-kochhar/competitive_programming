from collections import Counter

class Solution:
    def findDuplicates(self, arr):
        arr_dict = Counter(arr)
        ans = []
        
        for i,j in arr_dict.items():
            if j >1:
                ans.append(i)
        return (ans)