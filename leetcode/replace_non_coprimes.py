'''
Input: nums = [6,4,3,2,7,6,2]
Output: [12,7,6]
Explanation: 
- (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
- (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
- (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
- (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [12,7,6].
Note that there are other ways to obtain the same resultant array.
'''
import math 

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

nums = [6,4,3,2,7,6,2]
stack = []

for num in nums:
    stack.append(num)
    while len(stack) >= 2 and math.gcd(stack[-1], stack[-2]) > 1:
        b = stack.pop()
        a = stack.pop()
        stack.append(lcm(a, b))

print(stack)



