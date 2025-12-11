from collections import defaultdict

arr= [1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 5

arr_seen = defaultdict(list)
for i,j in enumerate(arr):
    arr_seen[j].append(i)

print(arr_seen)
res = []

(res.append(arr_seen[x][0]))
(res.append(arr_seen[x][-1]))

print(res)