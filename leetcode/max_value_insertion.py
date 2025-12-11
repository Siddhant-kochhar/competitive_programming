'''
Input: n = "99", x = 9
Output: "999"
Explanation: The result is the same regardless of where you insert 9.
'''

n = "-98"
x = 9

flag = True

if int(n) < 0:
    flag = False
else:
    flag = True

list_n = list(n)

if flag:
   
    for i in range(len(list_n)):
        if int(list_n[i]) < x:
            list_n.insert(i, str(x))
            break
    else:
        list_n.append(str(x))
else:
   
    for i in range(1, len(list_n)):  # Start from index 1 to skip the '-' sign
        if int(list_n[i]) > x:
            list_n.insert(i, str(x))
            break
    else:
        list_n.append(str(x))

print(''.join(list_n))
