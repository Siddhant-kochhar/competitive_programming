'''
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
'''

nums = [3,6,9,1]
nums.sort()

left = len(nums)-2
right = len(nums)-1
max_gap = 0

if len(nums) > 1:
    while left >=0:
        res = [nums[right],nums[left]]
        print(res)
