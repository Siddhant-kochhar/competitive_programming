'''
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.
Example 1:
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
'''

n = 9
nums = [i for i in range(1, n + 1)]
print(nums)
flag = True

while len(nums) > 1:
    if flag:
        # Left to right: keep every second element starting from index 1
        nums = [nums[i] for i in range(1, len(nums), 2)]
        flag = False
    else:
        # Right to left: reverse, keep every second element starting from index 1, then reverse back
        nums = [nums[i] for i in range(len(nums) - 2, -1, -2)]
        nums.reverse()
        flag = True

print(nums)