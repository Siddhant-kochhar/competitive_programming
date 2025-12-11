nums = [1,2,3,4,4,4,4,5,6,7]
k = 5

res = None

present_length = 0 
current_length = 1 

for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        current_length += 1
        res = min(current_length,present_length)
    else:
        present_length = current_length
        current_length = 1 
print(res)

if res >= k:
    print(True)
else:
    print(False)
