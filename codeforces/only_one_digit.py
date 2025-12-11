n = int(input())

for _ in range(n):
    x = int(input())
    x_list = list(str(x))
    x_list.sort()
    print(x_list[0])

