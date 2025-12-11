nums = [10,10,3,7,6]
count = 0 

prefix = [nums[0]]

for i in range(1,len(nums)):
    prefix.append(prefix[-1]+nums[i])

print(prefix)

left = 0 


while left < len(prefix)-1:
    if prefix[left]%2 == (prefix[-1] - prefix[left])%2:
        count += 1 
    left += 1 
print(count)