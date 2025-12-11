powers = set()
i = 1
while i < (1 << 50):  # large enough for 50-bit binaries
    powers.add(i)
    i *= 5

print(powers)

def solve(i):
    if i == len(s):
        return 0

    res = float('inf')
    num = 0

    for j in range(i, len(s)):
        num = num * 2 + int(s[j])
        if s[i] != '0' and num in powers:
            temp = solve(j + 1)
            if temp != float('inf'):
                res = min(res, 1 + temp)

    return res


ans = solve(0)
print(ans if ans != float('inf') else -1)
