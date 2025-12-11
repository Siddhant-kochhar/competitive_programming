import heapq

arr = [8, 6, 2]
total_sum = sum(arr)
half_sum = total_sum / 2  # target
steps = 0

# Convert to a max heap by pushing negative values
max_heap = [-x for x in arr]
heapq.heapify(max_heap)

current_sum = total_sum

# Keep halving largest elements until sum <= half of original
while current_sum >= half_sum:
    largest = -heapq.heappop(max_heap)
    half = largest / 2
    current_sum -= half
    heapq.heappush(max_heap, -half)
    steps += 1

print("Steps:", steps)
