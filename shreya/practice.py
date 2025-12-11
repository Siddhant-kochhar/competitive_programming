from collections import defaultdict

arr = [1,2,3,4]


arr_default_dict = defaultdict(int)
arr_dict = {1:0,2:0,3:0,4:0}

for i in arr:
    arr_default_dict[i] += 999

for i in arr:
    arr_dict[i] += 1 

print(arr_default_dict)

print(arr_dict)