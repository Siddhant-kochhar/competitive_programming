'''
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
'''
n = 1
res = []

for i in range(1,n//2+1):
    res.append(i)
    res.append(-i)

if n%2 != 0:
    res.append(0)
print(res)