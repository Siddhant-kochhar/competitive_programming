adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

res = []
queue = [0]

while queue:
    node = queue.pop(0)
    if node not in res:
        res.append(node)
    for neighbor in adj[node]:
        if neighbor not in res:
            queue.append(neighbor)

print(res)