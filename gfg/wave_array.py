arr = [1, 2, 3, 4, 5]

if len(arr) >1:
    for i in range(0,len(arr)-1,2):
        print(i)
        arr[i],arr[i+1] = arr[i+1],arr[i]

print(arr)