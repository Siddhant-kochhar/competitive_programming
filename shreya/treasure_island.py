from collections import defaultdict
import heapq

def solve():
    n, m, k = map(int, input().split())
    treasures = list(map(int, input().split()))
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    for _ in range(k):
        start, end = map(int, input().split())
        max_treasure, min_time = find_path(graph, treasures, start, end)
        print(max_treasure, min_time)

def find_path(graph, treasures, start, end):
    pq = [(-treasures[start-1], 0, start, frozenset([start]))]
    visited = {}
    best_treasure, best_time = 0, float('inf')
    
    while pq:
        neg_treasure, time, node, path = heapq.heappop(pq)
        treasure = -neg_treasure
        
        if node == end:
            if treasure > best_treasure or (treasure == best_treasure and time < best_time):
                best_treasure, best_time = treasure, time
            continue
        
        state = (node, path)
        if state in visited and visited[state] >= (treasure, -time):
            continue
        visited[state] = (treasure, -time)
        
        for next_node, travel_time in graph[node]:
            if next_node not in path:
                new_path = path | {next_node}
                new_treasure = treasure + treasures[next_node-1]
                new_time = time + travel_time
                heapq.heappush(pq, (-new_treasure, new_time, next_node, new_path))
    
    return best_treasure, best_time

solve()