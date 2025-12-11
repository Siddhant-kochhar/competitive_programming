'''
n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
'''
from collections import defaultdict
import itertools


n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]


graph = defaultdict(set)

for city1, city2 in roads:
    graph[city1].add(city2)
    graph[city2].add(city1)
res = 0
for city1, city2 in itertools.combinations(graph.keys(), 2):
    has_connection = 1 if city1 in graph[city2] else 0
    city1_connections = len(graph[city1])
    city2_connections = len(graph[city2])
    res = max(res, city1_connections + city2_connections - has_connection)
print(res)
