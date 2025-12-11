from collections import deque

res = {}
queue = deque([(root, 0)])

while queue:
    x,y = queue.popleft()
    res[y] = x.data

    if x.left:
        queue.append((x.left,y-1))
    if x.right:
        queue.append((x.right,y+1))
    
res = dict(sorted(res.items(),key = lambda x:x[0]))
final_res = []
for i in res:
    final_res.append(i)
print(final_res)