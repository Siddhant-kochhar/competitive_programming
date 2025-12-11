'''
edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
'''

from collections import defaultdict

edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

adj = defaultdict(list)

for i,j in edges:
    adj[i].append(j)
    adj[j].append(i)

print(adj)

visited = set()


def dfs(node, parent):
    visited.add(node)
    for nei in adj[node]:
        if nei not in visited:
            if dfs(nei, node):   # explore deeper
                return True
        elif nei != parent:      # visited and not parent → cycle
            return True
    return False

def has_cycle():
    for node in adj:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False

print(has_cycle())  # Output: True


