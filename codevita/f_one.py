import sys


def can_reach(race1, race2):
    """Check if a car can travel from race1 to race2"""
    x1, y1, d1 = race1
    x2, y2, d2 = race2
    
    # Calculate Manhattan distance
    distance = abs(x2 - x1) + abs(y2 - y1)
    
    # Check if there's enough time to travel
    time_available = d2 - d1
    
    return time_available >= distance


def find_matching(graph, n):
    """Find maximum matching in bipartite graph using DFS"""
    match = [-1] * n
    
    def dfs(u, visited):
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            # If v is not matched or we can find an augmenting path
            if match[v] == -1 or dfs(match[v], visited):
                match[v] = u
                return True
        return False
    
    matching_size = 0
    for u in range(n):
        visited = [False] * n
        if dfs(u, visited):
            matching_size += 1
    
    return matching_size


def min_cars_needed(races):
    """Calculate minimum number of cars needed for all races"""
    n = len(races)
    
    if n == 0:
        return 0
    
    # Sort races by day (important for DAG structure)
    races_with_idx = [(races[i][0], races[i][1], races[i][2], i) for i in range(n)]
    races_with_idx.sort(key=lambda x: (x[2], x[0], x[1]))
    
    # Rebuild races in sorted order
    sorted_races = [(x, y, d) for x, y, d, _ in races_with_idx]
    
    # Build adjacency list for bipartite matching
    # Edge from i to j means car can go from race i to race j
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            # Race i happens before or at same time as race j
            if sorted_races[i][2] <= sorted_races[j][2]:
                # Check if same day (can't use same car)
                if sorted_races[i][2] == sorted_races[j][2]:
                    continue
                
                # Check if car can reach from i to j
                if can_reach(sorted_races[i], sorted_races[j]):
                    graph[i].append(j)
    
    # Find maximum matching
    max_matching = find_matching(graph, n)
    
    # Minimum path cover = n - maximum matching
    return n - max_matching


# Read input
n = int(input())
races = []

for _ in range(n):
    line = list(map(int, input().split()))
    x, y, day = line[0], line[1], line[2]
    races.append((x, y, day))

# Calculate and print result
result = min_cars_needed(races)
sys.stdout.write(str(result) + '\n')