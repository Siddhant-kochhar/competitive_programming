t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())


def helper(c):

    if c % 2 != 0:
        if b > a:
            return "Second"
        else:
            return "First"
    else:
        if a > b:
            return "First"
        else:
            return "Second "
