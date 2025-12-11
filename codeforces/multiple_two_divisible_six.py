from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())

    cnt2 = 0
    cnt3 = 0
    temp = n

    while temp % 2 == 0:
        cnt2 += 1
        temp //= 2

    while temp % 3 == 0:
        cnt3 += 1
        temp //= 3

    if temp != 1 or cnt2 > cnt3:
        print(-1)
    else:
        # To reduce to 1:
        # - multiply by 2 (cnt3 - cnt2) times to match 3's, then divide by 6 cnt3 times
        print((cnt3 - cnt2) + cnt3)
