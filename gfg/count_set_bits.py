'''
Input: n = 4
Output: 5
Explanation: For numbers from 1 to 4. for 1: 0 0 1 => 1 set bit, for 2: 0 1 0 => 1 set bit, for 3: 0 1 1 => 2 set bits, for 4: 1 0 0 => 1 set bit. Therefore, the total set bits are 5.
Input: n = 17
Output: 35
Explanation: From numbers 1 to 17(both inclusive), the total number of set bits are 35.
'''

from collections import Counter

n = 4
res = 0 

for i in range(1,n+1):
    num = i
    num_split = list(bin(num))[2:]
    res += Counter(num_split)['1']
print(res)