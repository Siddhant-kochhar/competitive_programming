tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []
operations = ["+","-","*","/"]
for i in tokens:
    if i not in operations:
        stack.append(int(i))
        print(stack)
    else:
        x = int(stack.pop())
        y = int(stack.pop())
        print(x)
        print(y)

        if i == "+":
            stack.append((x+y))
            print(stack)
        elif i == "-":
            stack.append((y-x))
            print(stack)
        elif i == "*":
            stack.append((x*y))
            print(stack)
        elif i == "/":
            print("appending z")
            stack.append((y/x))
            print(stack)
        else:
            continue

print(int(stack[-1]))

