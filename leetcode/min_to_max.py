import heapq

N = 4
arr = [1, 2, 3, 4]


max_heap = [-i for i in arr]
heapq.heapify(max_heap)


res = []
while max_heap:
    res.append(-heapq.heappop(max_heap))
print(res)