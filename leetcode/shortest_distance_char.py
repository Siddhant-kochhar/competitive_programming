'''
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
'''

from collections import defaultdict

s = "loveleetcode"
c = "e"
res = []

c_index = []

for i,j in enumerate(s):
    if j == "e":
        c_index.append(i)

print(c_index)
res = []

for i,j in enumerate(s):
    temp = []
    for t in c_index:

        temp.append(abs(i-t))
    res.append(min(temp))
    temp.clear()


print(res)