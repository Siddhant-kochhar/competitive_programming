import heapq
import math

k = 2
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
origin = [0,0]

res = []
maxheap = []

for (x,y) in points:
    dist = math.sqrt((x - origin[0])**2 + (y - origin[1])**2)
    heapq.heappush(maxheap, (dist, [x,y]))
    
for _ in range(k):
    res.append(heapq.heappop(maxheap)[1])

print(res)