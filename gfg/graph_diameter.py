from collections import defaultdict

V = 7
E = 6
edges = [[0, 2], [0, 4], [0, 3], [3, 1], [3, 5], [1, 6]]
res = float('-inf')


adj = defaultdict(list)
for i,j in edges:
    adj[i].append(j)
    adj[j].append(i)

print(adj)

visited = set()
def dfs(node,visited,adj,count=0):
    global res
    if node not in visited:
        visited.add(node)
        count += 1
        for neighbor in adj[node]:
            dfs(neighbor,visited,adj,count)
    res= max(count,res)
print(dfs(0,visited,adj))
print(res)
