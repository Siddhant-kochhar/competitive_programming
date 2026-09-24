class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        final_res = []

        def digit_sum(num):
            res = 0

            while num > 0:
                last_digit = num % 10
                res += last_digit
                num = num // 10

            return res

            return num 

        for i,j in enumerate(nums):
            #print(i,j)
            x = digit_sum(j)
            #print(x)
            if x == i:
                final_res.append(i)

        if final_res:
            return (min(final_res))
        else:
            return (-1)