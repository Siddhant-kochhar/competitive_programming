edges = [[0,2],[0,3],[1,3],[2,3]]

edges_dict={i: 0 for i in range(len(edges))}
for u, v in edges:
    edges_dict[u] += 1

print(sum(edges_dict.values()))

