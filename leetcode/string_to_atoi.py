s = "1337c0d3"
list_s = list(s)
print(list_s)



stack = []
negative = False

for i in list_s:
    if i == "-" and not stack:
        negative = True
    elif i.isdigit():
        stack.append(i)
    else:
        break

if stack:
    x = "".join(stack)
    print (int("-" + x) if negative else int(x))
else:
    print(0)