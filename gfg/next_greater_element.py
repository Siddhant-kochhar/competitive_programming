'''
Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation:
The next greater element for 1 is 3.
The next greater element for 3 is 4.
The next greater element for 2 is 4.
The next greater element for 4 does not exist, so return -1.
'''

# x = [1, 5, 2, 4]
# res = []

# for i in range(len(x)):
#     next_greater = -1
#     for j in range((i + 1)%len(x), len(x)):
#         if x[j] > x[i]:
#             next_greater = x[j]
#             break
#     res.append(next_greater)

# print(res)



x = [1, 5, 2, 4]
n = len(x)
res = [-1] * n

stack = []

for i in range(2 * n):
    while stack and x[stack[-1]] < x[i % n]:
        idx = stack.pop()
        res[idx] = x[i % n]
    if i < n:
        stack.append(i)

print(res)

    