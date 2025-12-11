from collections import Counter
import heapq

arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
k = 4

max_heap = []
res = []
arr_dict = Counter(arr)

print(arr_dict)

for i,j in arr_dict.items():
    heapq.heappush(max_heap,(-j,-i))

for j in range(k):
    freq, num = heapq.heappop(max_heap)
    res.append(-num)

print(res)