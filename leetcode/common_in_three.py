arr1 = [1, 5, 10, 20, 40, 80] 
arr2 = [6, 7, 20, 80, 100] 
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

arr1 = set(arr1)
arr2 = set(arr2)
arr3 = set(arr3)

y = set.intersection(arr1,arr2,arr3)
print(sorted(list(y)))