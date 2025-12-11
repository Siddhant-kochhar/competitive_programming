def helper(arr):
    b = []
    c = []

    max_num = max(arr)
    for i in arr:
        if i != max_num:
            b.append(i)
        else:
            c.append(i)
    if b and c:
        return len(b), len(c), b, c
    else:
        return -1,

t = int(input())
for _ in range(t):
    n = int(input())  # size of arr
    arr = list(map(int, input().split()))
    
    res = helper(arr)
    if len(res) == 1:  # res[0] == -1
        print(-1)
    else:
        len_b, len_c, b, c = res
        print(len_b, len_c)
        print(*b)
        print(*c)
