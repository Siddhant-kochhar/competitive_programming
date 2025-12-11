from collections import Counter

arr = [6, 5, 8, 7, 1, 4, 1, 3, 2]

res = []
n = len(arr)

arr_dict = Counter(arr)
for key,value in arr_dict.items():
    if value ==2:
        res.insert(0,key)

total_sum = ((n * (n+1)//2))
current_sum = sum(arr)
res.append((total_sum-current_sum)+res[0])
print(res)