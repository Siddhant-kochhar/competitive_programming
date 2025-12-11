import heapq
from collections import defaultdict
res = []

def build_graph(tickets):
    graph = defaultdict(list)
    for src, dest in tickets:
        heapq.heappush(graph[src], dest)
    return graph

def dfs(graph, start):
    while graph[start]:
        next_dest = heapq.heappop(graph[start])
        dfs(graph, next_dest)
    res.append(start)


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
graph = build_graph(tickets)
dfs(graph, "JFK")
