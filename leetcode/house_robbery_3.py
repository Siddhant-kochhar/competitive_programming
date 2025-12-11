'''
class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
'''
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result = []
        if not root:
            return 0 
        else:
            q = deque([root])
            while q:
                level = []
                for i in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if level:
                    result.append(level)
        
        max_stolen = [0] * len(result)
        max_stolen = [0] * len(result)
        max_stolen[0] = result[0]
        max_stolen[1] = max(max_stolen[0],result[1])

        for i in range(2,len(result)):
            max_stolen[i] = max(max_stolen[i],max_stolen[i-2]+result[i])
        return max(max_stolen)




        