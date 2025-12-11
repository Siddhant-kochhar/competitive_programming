'''
a1 * a2 * a3 = 1 
a1+a2+a3 = 0 
'''

from collections import Counter

def helper(arr):
    res = 0 
    arr_dict = Counter(arr)
    values = list(arr_dict.values())  # Convert to list of counts
    if len(values) >= 2:
        res += abs(values[0] - values[1])
    res += max(values) % 2 if values else 0

    return res 

t = int(input())
for _ in range(t):
    n = int(input()) #size of arr
    x = list(map(int,input().split()))
    result = helper(x)
    print(result)
