class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0 

        while len(nums)>0:
            res = []
            elements_to_process = [i for i in nums if i !=0]
            

            if elements_to_process:
                min_element = min(elements_to_process)
            else:
                break
            for e in elements_to_process:
                if e - min_element > 0:
                    res.append(e-min_element)
                else:
                    continue
            op += 1
            nums.clear()
            nums += res
            res.clear()

        return(op)