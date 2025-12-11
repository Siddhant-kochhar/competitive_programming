import heapq

n = 4
m = 3
a = {10, 5, 6, 2}
b = {12, 7, 9}

# Combine both sets and create a max heap using negative values
combined = [-i for i in a] + [-j for j in b]

heapq.heapify(combined)


res = []
while combined:
    res.append(-heapq.heappop(combined))

print(res)