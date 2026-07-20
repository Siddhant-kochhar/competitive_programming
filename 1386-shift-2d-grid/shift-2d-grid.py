class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        vector = [element for row in grid for element in row]

        k %= len(vector)
        vector = vector[-k:] + vector[:-k]

        m, n = len(grid), len(grid[0])

        return [vector[i:i+n] for i in range(0, len(vector), n)]