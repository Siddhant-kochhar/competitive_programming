t = int(input())
for _ in range(t):
    size = int(input())
    x = list(map(int, input().split()))

    def helper(x):
        x.sort()
        if x[0] == x[-1]:
            print("NO")
        else:
            print("YES")
            # Swap the maximum element to the front
            max_num = x[-1]
            x.pop()            # remove last element
            x.insert(0, max_num)  # insert max at front
            print(*x)

    helper(x)
