'''
Input: n = 3, edges = [[0,1],[1,2]]
Output: 0
Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.
'''

n = 3
edges = [[0,1],[1,2]]

inorder = {i:0 for i in range(n)}
print(inorder)

for i,j in edges:
    inorder[j] += 1 

print(inorder)

res = []
for key,value in inorder.items():
    if value == 0:
        res.append(key)

if len(res)>1:
    print(-1)
else:
    print(res[-1])