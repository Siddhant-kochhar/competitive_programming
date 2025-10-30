class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        op = 0 
        op += target[0]
        for i in range(1,len(target)):
            if target[i-1] and target[i-1] < target[i]:
                op += abs(target[i-1] - target[i])
            else:
                op += 0 
        return op

