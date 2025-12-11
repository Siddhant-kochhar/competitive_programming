import heapq

n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]

adj = {}
for i in range(n):
    adj[i] = []

print(adj)

for edge in edges:
    src, des, weight = edge
    adj[src].append([des,weight])
    adj[des].append([src,weight])
print(adj)

minheap = []
for neig,weight in adj[0]:
    heapq.heappush(minheap,[weight,0,neig])
mst = []
visit = set()
visit.add(0)
while minheap:
    weight,src,node = heapq.heappop(minheap)
    if node in visit:
        continue
    mst.append([src,node,weight])
    visit.add(node)
    for neighbour,weight in adj[node]:
        heapq.heappush(minheap,[weight,node,neighbour])
print(mst)

res = 0 
for i in mst:
    res += i[-1]
print(res)
