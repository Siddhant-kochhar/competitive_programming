from collections import deque, defaultdict

edges = [[4,0],[5,0],[4,1],[3,1],[2,3],[5,2]]

# Find all unique nodes
all_nodes = set()
for u, v in edges:
    all_nodes.add(u)
    all_nodes.add(v)
n = len(all_nodes)

# Build adjacency list and indegree
adj = defaultdict(list)
indegree = {node: 0 for node in all_nodes}

for u, v in edges:
    adj[u].append(v)  # Fixed: u -> v, not v -> v
    indegree[v] += 1

print("Indegree:", indegree)

# Initialize queue with nodes having indegree 0
queue = deque()
for node in all_nodes:
    if indegree[node] == 0:
        queue.append(node)

print("Initial queue:", list(queue))

# Topological sort
res = []
while queue:
    x = queue.popleft()
    res.append(x)
    for neighbor in adj[x]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

# Check if topological sort is valid (no cycles)
if len(res) == n:
    print("Valid topological sort:", res)
    print(True)
else:
    print("Cycle detected! Only processed:", res)
    print(False)