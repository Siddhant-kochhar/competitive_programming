from collections import defaultdict

n = int(input())
s = input().strip()
two_grams = defaultdict(int)

for i in range(len(s)-1):
    x = (s[i:i+2])
    
    two_grams[x] += 1

two_grams = dict(sorted(two_grams.items(), key=lambda item: item[1], reverse=True))
for key,val in two_grams.items():
    print(key)
    break