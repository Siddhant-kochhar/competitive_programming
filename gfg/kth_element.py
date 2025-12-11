k = 10
a = [6, 6, 9, 10, 10, 11, 12]
b = [4, 5, 5, 6, 10, 11, 13]
a = sorted(set(a))  
b = sorted(set(b))  

first = 0 
second = 0 
res = float("inf")

for _ in range(k):
    if first < len(a) and second < len(b):
        if a[first] < b[second]:
            res = a[first]
            first += 1
        else:
            res = b[second]
            second += 1 
    elif first < len(a):  
        res = a[first]
        first += 1
    
    else:
        res = b[second]
        second += 1
print(res)