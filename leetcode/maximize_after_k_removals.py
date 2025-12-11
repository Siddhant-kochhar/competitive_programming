'''
Input: nums = [5,2,2,4,0,6], k = 4
Output: 5
Explanation:
One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
- Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
- Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
- Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
- Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
'''
nums = [5,2,2,4,0,6]
k = 4

buffer = []

for i in range(k-1):
    buffer.append(nums.pop(0))
print(buffer)


buffer.sort(reverse= True)

if len(nums) > 1:

    if nums[1] > buffer[0]:
        print(nums[1])
    else:
        buffer.sort(reverse = True)
        print(buffer[0])
else:
    




