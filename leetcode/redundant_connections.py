'''
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
'''

from collections import defaultdict

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

cycle = []

adj = defaultdict(list)

for i,j in edges:
    adj[i].append(j)
    adj[j].append(i)

print(adj)

visited = set()
def dfs(src, parent):
    visited.add(src)
    for nei in adj[src]:
        if nei == parent:
            continue  
        if nei not in visited:
            dfs(nei, src)
        else:
            cycle.append((src, nei))  


dfs(1, -1)
print(cycle[-1])