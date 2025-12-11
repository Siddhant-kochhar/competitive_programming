'''
Input : aaabsbbbeer
Output : 3a4b1s2e1r
Task was to find no. of characters in a string and output them in the this format : Total no. of characters in the string followed by that character
'''

from collections import Counter

x = "aaabsbbbeer"

x_dict = Counter(x)
print(x_dict)
x_dict = dict(sorted(x_dict.items(), key=lambda x: x[0]))
print(x_dict)
res = ""
seen = set(x)

for j in seen:
    res += str(x_dict[j])
    res += j

print(res)