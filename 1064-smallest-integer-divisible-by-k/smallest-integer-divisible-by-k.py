class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        res = 1 
        prev = set()

        while curr%k:
            rem = curr%k
            if rem in prev:
                res = -1
                break
            prev.add(rem)
            curr = rem*10 + 1
            res += 1
        return (res)