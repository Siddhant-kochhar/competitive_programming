'''
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
'''

from collections import defaultdict,deque

edges = [2,2,3,-1]
node1 = 0
node2 = 1

adj = defaultdict(list)

for i,dst in enumerate(edges):
    adj[i].append(dst)

print(adj)


def bfs(src,distMap):
    q = deque()
    q.append([src,0])
    distMap[src] = 0
    node,dist = q.popleft()
    for nei in adj[node]:
        if nei not in distMap:
            q.append([nei,dist+1])
            distMap[nei] = dist+1

node1Dist = {}
node2Dist = {}
bfs(node1,node1Dist)
bfs(node2,node2Dist)


res = -1 
resDist = float("inf")
for i in range(len(edges)):
    if i in node1Dist and i in node2Dist:
        dist = max(node1Dist[i],node1Dist[i])
        if dist < resDist:
            res = i
            resDist = dist
print(res)







node1Dist = {}
node2Dist = {}