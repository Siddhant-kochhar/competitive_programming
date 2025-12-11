n = int(input())
s = input().strip()
res = []
if len(s)%2 != 0:
    res.append(s[0])
    flag = True
    for i in range(1, len(s)):
        if flag:
            res.insert(0, s[i])
        else:
            res.append(s[i])
        flag = not flag
else:
    flag = False
    for i in range(len(s)):
        if not flag:
            res.insert(0, s[i])
        else:
            res.append(s[i])
        flag = not flag

print("".join(res))
