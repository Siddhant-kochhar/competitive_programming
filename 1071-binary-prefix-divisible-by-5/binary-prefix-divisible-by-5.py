class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = ""
        res = []

        for i in nums:
            num += str(i)
            if int(num,2)%5 ==0:
                res.append(True)
            else:
                res.append(False)
        return (res)