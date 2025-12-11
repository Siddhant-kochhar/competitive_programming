import heapq

arr = [4, 3, 2, 6]

res = 0

heapq.heapify(arr)
while len(arr) >1:
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    res += (x+y)
    heapq.heappush(arr,x+y)

print(res)
