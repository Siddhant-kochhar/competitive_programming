import heapq

n = 5
x = 0
k = 4
arr = [-21, 21, 4, -12, 20] 

heap = []

for house in arr:
    dist = abs(house - x)
    heapq.heappush(heap, (dist, -house)) 

    if len(heap) > k:
        heapq.heappop(heap)

result = [-pair[1] for pair in heap]  
print(sorted(result))