'''
Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
'''

x = [1, 2, 3, 7, 5]
target = 12

left = 0 
curr_sum = 0 
res = []

for right in range(len(x)):
    curr_sum += x[right]
    while curr_sum > target:
        curr_sum -= x[left]
        left +=1 
    if curr_sum == target:
        res = [left + 1, right + 1]
        break
print(res)
