import heapq

A = [3, 2]
B = [1, 4]
C = 2

max_heap = []

A.sort(reverse= True)
B.sort(reverse = True)

heapq.heappush(max_heap, (-(A[0] + B[0]), 0, 0))
visited = set((0, 0))
res = []

for _ in range(C):
    neg_sum,i,j = heapq.heappop(max_heap)
    res.append(-neg_sum)

    if i + 1 < len(A) and (i+1, j) not in visited:
            heapq.heappush(max_heap, (-(A[i+1] + B[j]), i+1, j))
            visited.add((i+1, j))
        
    # Next candidate: (i, j+1)
    if j + 1 < len(B) and (i, j+1) not in visited:
        heapq.heappush(max_heap, (-(A[i] + B[j+1]), i, j+1))
        visited.add((i, j+1))
        
print(res)