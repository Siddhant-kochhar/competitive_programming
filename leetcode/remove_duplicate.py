'''
Input: s = "bcabc"
Output: "abc"
'''
from collections import Counter 

s = "bcabc"

stack = []

s_dict = Counter(list(s))
print(s_dict)

seen = set()

for i in s:
    s_dict[i] -= 1 
    if i in seen:
        continue
    while stack and stack[-1] > i and s_dict[stack[-1]] > 0:
        seen.remove(stack[-1])
        stack.pop()
    stack.append(i)
    seen.add(i)

print("".join(stack))