num = -10

if num >0:
    print(num)
   
else:
    num_list = list(str(abs(num)))
    print(sorted(num_list, reverse = True))
    num_list.remove(max(num_list))
if num < 0:
    print(-1 * int("".join(num_list)))
else:
    print(int("".join(num_list)))