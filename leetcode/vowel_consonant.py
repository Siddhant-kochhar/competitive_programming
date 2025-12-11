from collections import defaultdict

s = "successes"
vowels = ["a","e","i","o","u"]

seen = defaultdict(int)
consonants = defaultdict(int)

for i in s:
    if i in vowels:
        seen[i] += 1 
    else:
        consonants[i] += 1 

seen = dict(sorted(seen.items(),key=lambda x:x[1],reverse = True))
consonants = dict(sorted(consonants.items(),key=lambda x:x[1],reverse = True))


print(seen)
print(consonants)

res = 0 
for key,value in seen.items():
    res += value 
    break 
for key,value in consonants.items():
    res += value
    break

print(res)