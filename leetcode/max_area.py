import math 

dimensions = [[9,3],[8,6]]
res = []

for i , j in dimensions:
    res.append(math.sqrt(i*i + j*j))

res_before = max(res)
x = res.index(res_before)

for i in range(len(dimensions)):
    if i == x:
        print(dimensions[i][0] * dimensions[i][1])
