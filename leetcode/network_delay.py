'''
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
'''
from collections import defaultdict
import heapq

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

edges = defaultdict(list)

for s,d,w in times:
    edges[s].append((d,w))

minheap = [(0,k)]
visit = set()
t = 0

while minheap:
    w1,n1 = heapq.heappop(minheap)
    if n1 in visit:
        continue
    visit.add(n1)
    t = max(t,w1)
    for n2,w2 in edges[n1]:
        if n2 not in visit:            
           heapq.heappush(minheap,[w2+w1,n2])

print(t) if len(visit) == n else - 1 
    