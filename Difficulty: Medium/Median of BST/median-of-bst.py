'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMedian(self, root):
        curr = root 
        stack = []
        res = []
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.data)
                curr = curr.right
        n = len(res)
        if n % 2 == 0:
            return res[(n // 2) - 1]
        else:
            return res[n // 2]