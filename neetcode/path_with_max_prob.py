from collections import defaultdict 
import heapq

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

adj = defaultdict(list)
for i,eq in enumerate(edges):
    x,y = eq
    adj[x].append((y, succProb[i]))  
    adj[y].append((x, succProb[i]))  

minheap = [(-1, start)]  
visited = set()

while minheap:
    w1, n1 = heapq.heappop(minheap)  
    current_prob = -w1  
    
    if n1 == end:
        print(current_prob)
        break
        
    if n1 in visited:
        continue
    visited.add(n1)
    
    for n2, w2 in adj[n1]:
        new_prob = current_prob * w2  
        heapq.heappush(minheap, (-new_prob, n2)) 