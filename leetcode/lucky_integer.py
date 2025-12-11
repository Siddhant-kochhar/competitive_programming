from collections import Counter

x = [1,2,2,3,3,3]
x_dict = Counter(x)
res = []

for key,value in x_dict.items():
    if key == value:
        res.append(key)
        print(res)

print(max(res))