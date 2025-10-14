class Solution:
    def nodeSum(self, root, l, r):
        res = 0
        curr = root
        stack = []
        
        while curr or stack:
            
            if curr is None:
                curr = stack.pop()
                continue
           
            if l <= curr.data <= r:
                res += curr.data

            if curr.right:
                stack.append(curr.right)

            curr = curr.left
        
        return res
