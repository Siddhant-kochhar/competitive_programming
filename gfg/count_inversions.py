x = [2, 4, 1, 3, 5]

cnt = 0 
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            cnt += 1 
print(cnt)
