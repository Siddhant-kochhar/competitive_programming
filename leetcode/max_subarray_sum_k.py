'''
Input: nums = [1,2], k = 1

Output: 3

Explanation:

The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.

Example 2:

Input: nums = [-1,-2,-3,-4,-5], k = 4

Output: -10

Explanation:

The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.

Example 3:

Input: nums = [-5,1,2,-3,4], k = 2

Output: 4

Explanation:

The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.

 Docstring for leetcode.max_subarray_sum_k
'''

nums = [-5,1,2,-3,4]
k = 2

prefix_sum = [nums[0]]   
last_sum = nums[0]
for i in range(1, len(nums)):
    last_sum += nums[i]
    prefix_sum.append(last_sum)
print(prefix_sum)

max_sum = float('-inf')
for L in range(k, len(nums)+1, k):   # <-- THE REAL FIX
    for j in range(L-1, len(prefix_sum)):
        if j == L-1:
            current_sum = prefix_sum[j]
        else:
            current_sum = prefix_sum[j] - prefix_sum[j - L]
        max_sum = max(max_sum, current_sum)
print(max_sum)