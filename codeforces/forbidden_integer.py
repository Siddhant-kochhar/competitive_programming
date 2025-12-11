t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())

    if x != 1:
        # Use 1's, since 1 ≠ x
        print("YES")
        print(n)
        print(' '.join(['1'] * n))
    else:
        if k == 1:
            # Cannot use anything if k == 1 and x == 1
            print("NO")
        elif k >= 2:
            if n % 2 == 0:
                # Use only 2's
                print("YES")
                print(n // 2)
                print(' '.join(['2'] * (n // 2)))
            else:
                if k >= 3:
                    # Use one 3, rest 2's
                    print("YES")
                    cnt = (n - 3) // 2
                    print(cnt + 1)
                    print(' '.join(['2'] * cnt + ['3']))
                else:
                    # k == 2, n odd, cannot partition
                    print("NO")
