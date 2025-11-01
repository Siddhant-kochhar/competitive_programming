class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)

        total = sum(beans)
        res = float('inf')

        for i in range(n):
            cost = total - (n - i) * beans[i]
            res = min(res, cost)
        return (res)