'''
Input: k = 2, arr[] = [1, 5, 8, 10]
Output: 5
Explanation: The array can be modified as [1+k, 5-k, 8-k, 10-k] = [3, 3, 6, 8]. The difference between the largest and the smallest is 8-3 = 5.
Input: k = 3, arr[] = [3, 9, 12, 16, 20]
Output: 11
Explanation: The array can be modified as [3+k, 9+k, 12-k, 16-k, 20-k] = [6, 12, 9, 13, 17]. The difference between the largest and the smallest is 17-6 = 11. 
'''



k = 7
arr = [7,1,8,10,6,4,6,9,1]
n = len(arr)


arr.sort()
ans = arr[-1] - arr[0]
smallest = arr[0] + k
largest = arr[-1] - k

for i in range(n - 1):
        mi = min(smallest, arr[i+1] - k)
        ma = max(largest, arr[i] + k)
        if mi < 0:
            continue
        ans = min(ans, ma - mi)

print(ans)