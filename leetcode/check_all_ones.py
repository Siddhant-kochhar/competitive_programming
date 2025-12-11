nums = [1,0,0,1,0,1]
k = 2

one_positions = [i for i, num in enumerate(nums) if num == 1]
print(one_positions)
res = True

for i in range(1, len(one_positions)):
    if one_positions[i] - one_positions[i-1] - 1 < k:
        res = False
        break
print(res)