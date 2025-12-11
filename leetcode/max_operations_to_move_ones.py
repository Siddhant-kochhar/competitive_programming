s = "1001101"


one_count = 0 
res = 0 
i = 0 

while i < len(s):
    if s[i] == '1':
        one_count += 1
    else:
        res += one_count
        while i+1<len(s) and s[i+1] == '0':
            i += 1
    i += 1
print(res)
    