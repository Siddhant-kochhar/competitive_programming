arr = [1, 10, 12, 13, 14]
x = 2 


res = []
for l in range(len(arr)):
    curr = [arr[l]]  # Move this BEFORE inner loop
    for r in range(l+1, len(arr)):
        if abs(arr[r] - arr[l]) <= x:
            curr.append(arr[r])
        else:
            break
    res.append(curr.copy())  # Append after inner loop finishes
print(res)


res = sorted(res,key = lambda x:len(x),reverse = True)
print(res[0])