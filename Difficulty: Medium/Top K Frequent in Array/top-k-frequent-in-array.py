from collections import Counter
import heapq

class Solution:
	def topKFreq(self, arr, k):
		# Code here
		
        max_heap = []
        res = []
        arr_dict = Counter(arr)
        
        #print(arr_dict)
        
        for i,j in arr_dict.items():
            heapq.heappush(max_heap,(-j,-i))
        
        for j in range(k):
            freq, num = heapq.heappop(max_heap)
            res.append(-num)
        
        return (res)