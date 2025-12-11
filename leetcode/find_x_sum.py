'''
Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
'''

from collections import Counter
import heapq 


nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2

l = 0
window = nums[l:l+k]    
count = Counter(window)
max_heap = [(-freq, -num) for num, freq in count.items()]
heapq.heapify(max_heap)
result = []
result.append(sum([-num * -freq for freq, num in heapq.nsmallest(x, max_heap)]))

for r in range(k,len(nums)):
    left_num = nums[l]
    count[left_num] -= 1
    if count[left_num] ==0:
        del count[left_num]
    right_num = nums[r]
    count[right_num] += 1
    max_heap = [(-freq, -num) for num, freq in count.items()]
    heapq.heapify(max_heap)
    result.append(sum([-num * -freq for freq, num in heapq.nsmallest(x, max_heap)]))

    l += 1
print(result)
