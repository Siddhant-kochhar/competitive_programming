x = [1,2,3,4,5]
print("array",x)
print(x[2])


y = [0] * 15
print(y)

z = {1,2,3,4,5,6,6}
print(z)


t = [1,2,3,4,5,6,6]
t = set(t)
print("output",t)

array_dict = {"apple":1,"banana":2}
print(array_dict)
print(array_dict["apple"])
print(array_dict.items())

for judgesahab,heaven in array_dict.items():
    print(judgesahab)
    print(heaven)

r = [1,2,3,4,5,6,7,8,9]
for i,j in enumerate(r):
    print(i,j)


u = [1,2,3,4,5,6,7]
q = [8,9,10,11,12,13,14]

print("###############")

# (1,8) (2,9) (3,10)

res = []
for h,k in zip(u,q):
    print(h,k)
    res.append((h,k))
print(res)

from collections import deque

q = deque()
q.append(1)
q.append(2)
print(q)
print(q.popleft())



