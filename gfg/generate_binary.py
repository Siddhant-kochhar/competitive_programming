'''
Input: n = 4
Output: ["1", "10", "11", "100"]
Explanation: Binary numbers from 1 to 4 are 1, 10, 11 and 100.
'''

n = 4
res = []
for i in range(1,n+1):
    res.append(bin(i)[2:])

print(res)