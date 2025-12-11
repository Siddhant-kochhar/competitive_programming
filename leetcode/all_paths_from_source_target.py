'''
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
'''

graph = [[1,2],[3],[3],[]]

n = len(graph)
result = []

def dfs(city,curr):
    for nei in range(n):
        if nei in graph[city]:
            curr.append(nei)
            if nei == n-1:
                result.append(curr[:])
            else:
                dfs(nei,curr)
            curr.pop()

dfs(0,[0])
print(result)   