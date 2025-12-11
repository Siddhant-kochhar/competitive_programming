classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
# Output: 0.78333

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        import heapq

        heap = []

        for passes, total in classes:
            current_ratio = passes / float(total)
            improvement = (passes + 1) / float(total + 1) - current_ratio
            heapq.heappush(heap, (-improvement, passes, total))

        for _ in range(extraStudents):
            improvement, passes, total = heapq.heappop(heap)
            passes += 1
            total += 1
            current_ratio = passes / float(total)
            new_improvement = (passes + 1) / float(total + 1) - current_ratio
            heapq.heappush(heap, (-new_improvement, passes, total))

        total_ratio = 0.0
        while heap:
            _, passes, total = heapq.heappop(heap)
            total_ratio += passes / float(total)

        return total_ratio / len(classes)
