from itertools import combinations


n = 9
k = 3

digits_can_use = [1,2,3,4,5,6,7,8,9]
print(digits_can_use)

res = set()

comb = combinations(digits_can_use,k)
for j in comb:
    #print(j)
    if sum(j) == n:
        res.add(j)
    else:
        continue
print(res)


# from itertools import combinations

# n = 9
# k = 3

# digits_can_use = [1,2,3,4,5,6,7,8,9]
# print(digits_can_use)

# res = []

# comb = combinations(digits_can_use, k)
# for j in comb:
#     if sum(j) == n:
#         res.append(j)

# print(res)