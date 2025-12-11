num = 9669
num_str = str(num)
for i in num_str:
    if i == '6':
        num_str = num_str.replace(i, '9', 1)
        break
print(num_str)
print(int(num_str))