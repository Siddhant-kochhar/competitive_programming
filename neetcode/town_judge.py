'''


Input: n = 4, trust = [[1,3],[4,3],[2,3]]

Output: 3

'''

n = 4
trust = [[1,3],[4,3],[2,3]]


outdegree = [0] * (n+1)
indegree = [0] * (n+1)

for a,b in trust:
    outdegree[a] += 1
    indegree[b] += 1

for i in range(1, n+1):
    if outdegree[i] == 0 and indegree[i] == n-1:
        print(i)
        break