'''
Input: arr[] = [-8, 2, 3, -6, 10] , k = 2
Output: [-8, 0, -6, -6]
Explanation:
Window [-8, 2] First negative integer is -8.
Window [2, 3] No negative integers, output is 0.
Window [3, -6] First negative integer is -6.
Window [-6, 10] First negative integer is -6.
'''

arr = [-8, 2, 3, -6, 10] 
k = 2
n = len(arr)

res = []

l = 0 

for r in range(n - k + 1):
    window = arr[r:r+k]
    print(window)
    first_neg = 0 
    for num in window:
        if num < 0:
            first_neg = num
            break
    res.append(first_neg)
    
print(res)


arr = [-8, 2, 3, -6, 10] 
k = 2
n = len(arr)

from collections import deque

res = []
neg_idx = deque()  # stores indices of negative numbers

for i in range(n):
    # Add current element index if it is negative
    if arr[i] < 0:
        neg_idx.append(i)
    # Remove indices out of the current window
    if neg_idx and neg_idx[0] < i - k + 1:
        neg_idx.popleft()
    # Start recording results when the first window is complete
    if i >= k - 1:
        if neg_idx:
            res.append(arr[neg_idx[0]])
        else:
            res.append(0)

print(res)