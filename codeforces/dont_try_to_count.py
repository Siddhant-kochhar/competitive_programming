def check(s, x):
    # Check if s is a substring of x
    return s in x

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()

    # Create strings after 0 to 5 operations
    x0 = x                # 0 operations
    x1 = x0 + x0          # 1 operation
    x2 = x1 + x1          # 2 operations
    x3 = x2 + x2          # 3 operations
    x4 = x3 + x3          # 4 operations
    x5 = x4 + x4          # 5 operations

    ans = -1

    if check(s, x0):
        ans = 0
    elif check(s, x1):
        ans = 1
    elif check(s, x2):
        ans = 2
    elif check(s, x3):
        ans = 3
    elif check(s, x4):
        ans = 4
    elif check(s, x5):
        ans = 5

    print(ans)
