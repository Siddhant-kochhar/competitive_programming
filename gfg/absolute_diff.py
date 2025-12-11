import heapq

x = 7
arr = [10, 5, 3, 9, 2]

min_heap = []

for i , j in enumerate(arr):
    heapq.heappush(min_heap, (abs(j - x),j))

print(min_heap)
res = []
while min_heap:
    diff, value = heapq.heappop(min_heap)
    res.append(value)
print(res)
