'''
Input: s = "leetcoder"
'''

s = "leetcoder"

vowels = ["a","e","i","o","u"]

seen = []

for j in (s):
    if j in vowels:
        seen.append(j)
    
print(seen)