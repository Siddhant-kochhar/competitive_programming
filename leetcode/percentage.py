from collections import Counter

s = "foobar"
letter = "o"

n = len(s)
seen = Counter(s)
print(seen)
print(seen.keys())
if letter not in seen.keys():
    print(0) 
else:
    print((seen[letter]/n) * 100)