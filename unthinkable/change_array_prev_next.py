arr = [1,2,3,4,5,6,7,8,9]
res = []
for i in range(1,len(arr)-1):
    prev_elem = arr[i-1]
    next_elem = arr[i+1]
    res.append((prev_elem+next_elem))

print(res)