arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

count = 0 
L = 0 

for R in range(len(arr)):
    if R-L+1 == k:
        if (sum(arr[L:R+1]))/k >= threshold:
            count += 1
        L += 1

print(count)    