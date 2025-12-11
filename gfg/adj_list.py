# from collections import defaultdict

# edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
# adj_list = defaultdict(list)

# for u,v in edges:
#     adj_list[u].append(v)
#     adj_list[v].append(u)

# # print(adj_list)
# res = []
# for i in adj_list:
#     res.append(i)
# print(res)


from typing import List
from collections import defaultdict

class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize adjacency list with empty lists for all vertices
        adj_list = [[] for _ in range(V)]
        
        # Build the adjacency list
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Sort the neighbors for each vertex
        for i in range(V):
            adj_list[i].sort()
        
        return adj_list

edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
print(Solution().printGraph(5, edges))