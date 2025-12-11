'''
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
'''
from collections import defaultdict

nums = [0,1,1,1,0,1,1,0,1]
left = 0

nums_dict = defaultdict(int)
max_length = 0

for right in range(len(nums)):
    nums_dict[nums[right]] += 1       
    while nums_dict[0] > 1:
        nums_dict[nums[left]] -= 1
        left += 1
    max_length = max(max_length, right - left)

print(max_length)   



from collections import defaultdict

def longestSubarray(nums):
    left = 0
    max_length = 0
    zero_count = 0
    
    for right in range(len(nums)):
        # Count zeros
        if nums[right] == 0:
            zero_count += 1
        
        # Shrink the window if we have more than one zero
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Update max length (subtract 1 because we're deleting one element)
        max_length = max(max_length, right - left)
    
    return max_length

# Test with your example
nums = [0,1,1,1,0,1,1,0,1]
result = longestSubarray(nums)
print(result)  # Output: 5