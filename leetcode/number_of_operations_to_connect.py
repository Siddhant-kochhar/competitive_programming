'''
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
'''

n = 4
connections = [[0,1],[0,2],[1,2]]
m = len(connections)
keys = {i:[] for i in range(n)}
print(keys)

length_of_connections = len(connections)

if length_of_connections == n - 1:
    for i,j in connections:
        keys[i].append(j)
        keys[j].append(i)
    print(keys)

    cnt = 0 

    for key,value in keys.items():
        if value == []:
            cnt += 1
    print(cnt)
else:
    print(-1)

