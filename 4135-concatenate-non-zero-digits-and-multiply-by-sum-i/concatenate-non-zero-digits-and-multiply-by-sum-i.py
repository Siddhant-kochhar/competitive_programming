class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = "".join([i for i in str(n) if i != '0'])
        if not x:
            return 0 
        sum_digits = sum(int(i) for i in x)
        result = int(x) * sum_digits
        
        return (result)