from collections import Counter

class Solution:
    def findTwoElement(self, arr):
        res = []
        n = len(arr)
        
        arr_dict = Counter(arr)
        for key,value in arr_dict.items():
            if value ==2:
                res.insert(0,key)
        
        total_sum = ((n * (n+1)//2))
        current_sum = sum(arr)
        res.append((total_sum-current_sum)+res[0])
        return (res)