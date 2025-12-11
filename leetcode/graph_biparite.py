from collections import deque, defaultdict

# Build adjacency list from edges
def build_adj_list(edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  # For undirected graph
    return adj

def isBipartite(adj):
    color = {}  # Store color for each node: 0 or 1
    
    for node in adj:
        if node not in color:
            # Start BFS from this uncolored node
            queue = deque([node])
            color[node] = 0  # Assign initial color
            
            while queue:
                current = queue.popleft()
                
                for neighbor in adj[current]:
                    if neighbor not in color:
                        # Assign opposite color
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        # Conflict found - same color for adjacent nodes
                        return False
    return True