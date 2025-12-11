'''
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
'''

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

keys = {i:[] for i in range(n)}
for i,j in edges:
    keys[i].append(j)
    keys[j].append(i)
print(keys)

res = []

def dfs(i):
    visited = set()
    curr_res = 1
    if i not in visited:
        visited.add(i)
        
        dfs(i)

