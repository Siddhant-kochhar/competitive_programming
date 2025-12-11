from collections import defaultdict




nums =[1,2,2,3,3,4]
k = 2

nums.sort()
used = defaultdict(bool)
max_used = float('-inf')

for num in nums:
    start = num - k
    end = num + k

    candidate = max(start,max_used + 1)

    while candidate <= end:
        if not used[candidate]:
            used[candidate] = True
            max_used = candidate 
            break
        candidate +=1 
print(used) 
print((used.values()))