beans = [4,1,6,5]
beans.sort()
n = len(beans)

total = sum(beans)
res = float('inf')

for i in range(n):
    cost = total - (n - i) * beans[i]
    res = min(res, cost)
print(res)