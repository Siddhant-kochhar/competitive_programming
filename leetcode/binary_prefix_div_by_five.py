'''
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
'''

nums = [1,1,1]
num = ""
res = []

for i in nums:
    num += str(i)
    if int(num)%5 ==0:
        res.append(True)
    else:
        res.append(False)
print(res)