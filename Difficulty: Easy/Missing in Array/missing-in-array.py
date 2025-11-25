class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1 
        total_sum = (n*(n+1)) / 2
        current_sum = sum(arr)
        missing_num = total_sum - current_sum
        return int(missing_num)