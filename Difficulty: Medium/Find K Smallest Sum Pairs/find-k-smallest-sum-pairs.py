import heapq

class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        # code here
    
        minheap = []
        result = []
        
        a_len, b_len = len(arr1), len(arr2)
        
        if a_len < b_len:
            # seed along i with j=0
            for i in range(min(a_len, k)):
                heapq.heappush(minheap, (arr1[i] + arr2[0], i, 0))
        else:
            # seed along j with i=0
            for j in range(min(b_len, k)):
                heapq.heappush(minheap, (arr1[0] + arr2[j], 0, j))
        
        while minheap and len(result) < k:
            _, i, j = heapq.heappop(minheap)
            result.append([arr1[i], arr2[j]])
            if a_len < b_len:
                # expand to next in row (increase j)
                if j + 1 < b_len:
                    heapq.heappush(minheap, (arr1[i] + arr2[j + 1], i, j + 1))
            else:
                # expand to next in column (increase i)
                if i + 1 < a_len:
                    heapq.heappush(minheap, (arr1[i + 1] + arr2[j], i + 1, j))
        
        return (result)