arr = [10, 20, 15, 2, 23, 90, 80]

for i,j in enumerate(arr):
    if i == 0:
        if j > arr[i+1]:
            print(i)
            break
    elif i == len(arr)-1:
        if j > arr[i-1]:
            print(i)
            break
    else:
        if j > arr[i+1] and j > arr[i-1]:
            print(i)
            break
        else:
            continue
