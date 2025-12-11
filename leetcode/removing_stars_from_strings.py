'''
Input: s = "leet**cod*e"
Output: "lecoe"
'''

s = "leet**cod*e"
stack = []

for char in s:
    if char == '*':
        if stack:
            stack.pop()
            continue
    stack.append(char)
print(''.join(stack))

