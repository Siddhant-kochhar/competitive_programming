class Solution:
    def minOperations(self, arr):
        import heapq

        total_sum = sum(arr)
        half_sum = total_sum / 2
        steps = 0

        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        current_sum = total_sum

        while current_sum > half_sum:
            largest = -heapq.heappop(max_heap)
            half = largest / 2
            current_sum -= half
            heapq.heappush(max_heap, -half)
            steps += 1

        return steps
