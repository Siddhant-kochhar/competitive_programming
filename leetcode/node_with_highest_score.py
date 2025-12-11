'''
Input: edges = [1,0,0,0,0,7,7,5]
Output: 7
Explanation:
- The nodes 1, 2, 3 and 4 have an edge pointing to node 0. The edge score of node 0 is 1 + 2 + 3 + 4 = 10.
- The node 0 has an edge pointing to node 1. The edge score of node 1 is 0.
- The node 7 has an edge pointing to node 5. The edge score of node 5 is 7.
- The nodes 5 and 6 have an edge pointing to node 7. The edge score of node 7 is 5 + 6 = 11.
Node 7 has the highest edge score so return 7.
'''

edges = [1,0,0,0,0,7,7,5]

adj = {i:[] for i in range(len(edges))}

print(adj)

for i,j in enumerate(edges):
    adj[j].append(i)

print(adj)

key, value = max(adj.items(), key=lambda x: sum(x[1]))
print(key)


