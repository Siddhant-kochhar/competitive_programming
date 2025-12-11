a = 5
b = -2 
c = -4
N = 14
updated_n = N - 3 

first_diff = b - a
second_diff = c - b
res = [0] * N 
res[0] = a
res[1] = b 
res[2] = c 
j = 3 


for i in range(updated_n):
    if j%2 !=0:
        res[j] = res[j-1] + first_diff
        j += 1
    else:
        res[j] = res[j-1] + second_diff
        j += 1

print(res[-1])