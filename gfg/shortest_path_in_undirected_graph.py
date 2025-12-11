'''
Input: adj[][] = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]], src=0
Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
'''

import heapq

adj = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
src=0


mat = {i:[] for i in range(len(adj))}

print(mat)

for i,j in enumerate(adj):
    for t in j:
        mat[i].append(t)

print(mat)



shortest = {}

minheap = [(0,src)]

while minheap:
    w1,n1 = heapq.heappop(minheap)

    if n1 in shortest:
        continue
    shortest[n1] = w1 

    for nei in adj[n1]:
        if nei not in shortest:
            heapq.heappush(minheap,(w1+1,nei))

res = [-1] * len(adj)
for key, value in shortest.items():
    res[key] = value

print(res)