class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0
        for i in range(len(plants)):
            if water < plants[i]:
                steps += 2 * i
                water = capacity
            water -= plants[i]
            steps += 1
        return steps