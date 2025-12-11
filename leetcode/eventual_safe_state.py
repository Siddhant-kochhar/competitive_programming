graph = [[1,2],[2,3],[5],[0],[5],[],[]]
nodes = {i:[] for i in range(len(graph))}

for i in range(len(graph)):
    for x in graph[i]:
        nodes[i].append(x)

print(nodes)

# find terminal nodes
terminal_nodes = [k for k,v in nodes.items() if not v]
print(terminal_nodes)

safe_nodes = []

for z, t in nodes.items():
    # if all neighbors are terminal nodes
    if t and all(neigh in terminal_nodes for neigh in t):
        safe_nodes.append(z)

# safe nodes = those + terminal nodes
safe_nodes.extend(terminal_nodes)
print(sorted(safe_nodes))
