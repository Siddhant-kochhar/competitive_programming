import heapq 

arr1 = [1, 7, 11]
arr2 = [2, 4, 6]
k = 3

minheap = []
result = []

a,b = len(arr1), len(arr2)


if a < b:

    for i in range(min(a,k)):
            heapq.heappush(minheap, (a[i] + b[0], i, 0))
else:
    for j in range(min(b,k)):
            heapq.heappush(minheap, (a[0] + b[j], 0, j))


while minheap and len(result) < k:
        _, i, j = heapq.heappop(minheap)
        result.append([a[i], b[j]])
        if j + 1 < b:
            heapq.heappush(minheap, (a[i] + b[j + 1], i, j + 1))

print(result)