n = int(input())
arr = list(map(int,input().split()))

def helper(arr):
    res = []
    for i in arr:
        if i < 0 :
            res.append(abs(i))
        else:
            res.append(i)
    res.sort()
    return res[0]

print(helper(arr))

