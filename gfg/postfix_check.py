arr = ["-8", "3", "/"]

stack = []
operators = ["+","-","*","/","^"]

for i in arr:
    if (i) not in operators:
        stack.append(i)
    else:
        x = int(stack.pop())
        y = int(stack.pop())
        if i == "+":
            stack.append(x+y)
        elif i == "*":
            stack.append(x*y)
        elif i == "-":
            stack.append(y-x)
        elif i== "/":
            stack.append(y//x)
        else:
            stack.append(y**x)
if stack:
    print(stack[0])
else:
    print(-1)

