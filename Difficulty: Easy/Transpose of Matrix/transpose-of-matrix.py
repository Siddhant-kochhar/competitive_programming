class Solution:
    def transpose(self, mat):
        # code here
        res = [tuple(row) for row in zip(*mat)]
        return res
