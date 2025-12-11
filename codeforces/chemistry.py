from collections import Counter

t = int(input())  # number of test cases
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    freq = Counter(s)

    # count how many chars have odd frequency
    odd_count = sum(1 for v in freq.values() if v % 2 != 0)

    # We can use deletions to fix odd counts
    # Condition:
    # - odd_count - k <= 1  (we can fix enough odd counts)
    # - and (n - k) > 0     (non-empty string after deletion)
    if odd_count - k <= 1 and (n - k) > 0:
        print("YES")
    else:
        print("NO")
