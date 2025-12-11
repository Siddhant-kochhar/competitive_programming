'''
equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

'''
from collections import defaultdict,deque

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]

queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

adj = defaultdict(list)

for i,eq in enumerate(equations):
   x,y = eq
   adj[x].append([y,values[i]])
   adj[y].append([x,1/values[i]])

print(adj)

def dfs(src,target):
   if src not in adj or target not in adj:
      return -1 
   q,visit = deque(),set()
   q.append([src,1])
   visit.add(src)
   while q:
      n , w = q.popleft()
      if n == target:
         return w 
      for nei,weight in adj[n]:
         q.append([n,w*weight])
         visit.add(nei)
   return -1 

def evaluate_division():
   return [dfs(q[0],q[1]) for q in queries]

result = evaluate_division()
print(result)
