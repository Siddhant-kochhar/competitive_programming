arr = [1,2,4]
curr = set()
prev = set()
res = set()

n = len(arr)

for i in range(n):
    if prev:
        for j in prev:
            curr.add(i | j)
            res.add(i | j)
    else:
        curr.add(i)
        res.add(i)
    
    prev = curr 
    curr.clear()
print(len(res))

