from collections import Counter

N = 6

array = {1, 1, 1, 2, 2, 3}
array = list(array)
K = 2

seen = Counter(array)


seen = dict(sorted(seen.items(), key=lambda x: x[1], reverse=True))

res = []
while K > 0:
    for key,value in seen.items():
        res.append(key)
        K -= 1

print(res)