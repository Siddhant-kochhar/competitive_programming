'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
import heapq

class Solution:
    def kthSmallest(self, root, k): 
        # code here
        stack = []
        curr = root
        res = []
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                heapq.heappush(res,curr.data)
                curr = curr.right
        if res and len(res) >= k:
            for j in range(k):
                t = heapq.heappop(res)
            return t
        
        return -1 