'''
Input: arr[] = [1, 3, 3]
Output: [[1, 3, 3], [3, 1, 3], [3, 3, 1]]
Explanation: These are the only possible distinct permutations for the given array.
'''
from itertools import permutations

arr = [1, 3, 3]

x = permutations(arr,len(arr))

res = set()
for i in x:
    res.add(i)

print(sorted(res))