x = (input())
y = (input())
res = []

x_list = list((x))
y_list = list((y))

# print(x_list)  # ['1', '0', '1', '0', '1', '0', '0']
# print(y_list)  # ['0', '1', '0', '0', '1', '0', '1']

for i,y in zip(x_list, y_list):
    if i ==y:
        res.append("0")
    else:
        res.append("1")
print(("".join(res)))