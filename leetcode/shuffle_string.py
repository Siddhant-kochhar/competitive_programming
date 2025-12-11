'''
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
'''

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

s_split = list(s)
seen = {}

for i,j in zip(s_split,indices):
    seen[j] = i 

print(seen)

seen = dict(sorted(seen.items(), key=lambda x: x[0]))
print(seen)

res = []
for i,j in seen.items():
    res.append(j)

print("".join(res))