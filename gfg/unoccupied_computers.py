n = 3
s = "CFIJEADGCFHGEDBBIHJA"

s_set = set(s)
allocated = {i:False for i in s_set}
res = set()


for i in s:
    if n > 0:
        if allocated[i]:
            n += 1 
            allocated[i] = False
        else:
            n -= 1 
            allocated[i] = True
    else:
        if allocated[i]:
            allocated[i] = False
            n += 1 
        else:
            res.add(i)
print(len(res))