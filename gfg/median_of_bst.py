curr = root 
stack = []
res = []

while stack or curr:
    if curr:
        stack.append(curr)
        curr = curr.left
    else:
        curr = stack.pop()
        res.append(curr.data)
        curr = curr.right
