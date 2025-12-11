'''
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
'''

k = 1

res = 1 
prev = set()

while res%k !=0:
    rem = res%k
    if rem in prev:
        res = -1
        break
    prev.add(rem)
    res = rem*10 + 1
    res += 1
print(res)


