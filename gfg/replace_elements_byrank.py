import heapq
from collections import defaultdict

class Solution:
    def replaceWithRank(self, N, arr):
        # Create a min-heap with all unique elements
        unique_elements = list(set(arr))
        heapq.heapify(unique_elements)
        
        # Create rank mapping
        rank_map = {}
        current_rank = 1
        
        while unique_elements:
            element = heapq.heappop(unique_elements)
            rank_map[element] = current_rank
            current_rank += 1
        
        # Replace each element with its rank
        return [rank_map[num] for num in arr]