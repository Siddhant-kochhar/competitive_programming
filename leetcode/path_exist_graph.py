'''
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
'''

from collections import defaultdict

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

adj = defaultdict(list)

for i,j in edges:
    adj[i].append(j)
    adj[j].append(i)

print(adj)


def dfs(node, visited):
    if node == destination:
        return True
    visited.add(node)
    for j in adj[node]:
        if j not in visited:
            if dfs(j, visited):
                return True
    return False

result = dfs(source, set())
print(result)
