arr = [1, 2, 0, 3]

n = len(arr)

pre = [0] * n 
suff = [0] * n 
res = float("-inf")

left = 0 
right = 0 

for i in range(n):
    pre[i] = arr[i] + left 
    left = pre[i]

print(pre)

for j in range(n-1,-1,-1):
    suff[j] = arr[j] + right
    right = suff[j]

print(suff)

for t in range(n):
    if pre[t] == suff[t]:
        print(t)
        