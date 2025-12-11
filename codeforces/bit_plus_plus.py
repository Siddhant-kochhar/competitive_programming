n = int(input())
res = 0 
for i in range(n):
    sample = input()
    if "+" in sample:
        res += 1
    else:
        res -= 1
print(res)