'''
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

from collections import defaultdict

nums = [1,1,1,2,2,3]

def remove_duplicates(nums):
    x = defaultdict(int)
    left = 0 
    right = len(nums) - 1

    while left <= right:
        x[nums[left]] += 1
        if x[nums[left]] > 2:
            nums.pop(left)
            right -= 1
        else:
            left += 1
    return nums

print(remove_duplicates(nums))