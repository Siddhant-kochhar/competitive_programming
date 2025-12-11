from collections import Counter

s = "abcc"
k = 2
count = 0
i = 0

while i <= len(s) - 3:
    substr = s[i:i+3]
    if len(Counter(substr)) == k:
        count += 1
    i += 1

print(count)