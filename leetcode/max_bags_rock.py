'''
Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Output: 3
Explanation:
Place 1 rock in bag 0 and 1 rock in bag 1.
The number of rocks in each bag are now [2,3,4,4].
Bags 0, 1, and 2 have full capacity.
There are 3 bags at full capacity, so we return 3.
It can be shown that it is not possible to have more than 3 bags at full capacity.
Note that there may be other ways of placing the rocks that result in an answer of 3.
'''
capacity = [10,2,2]
rocks = [2,2,0]
additionalRocks = 100

max_capacity = []
for i,j in zip(capacity,rocks):
    max_capacity.append(i-j)
print(max_capacity)

max_capacity.sort()
cnt = max_capacity.count(0)
print(cnt)
for z in max_capacity:
    if z >0:
        if (additionalRocks-z) >= 0:
            cnt += 1
            additionalRocks -= z

print(cnt)
