matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

found = False
for i in matrix:
    if i[-1] >= target >= i[0]:
        if target in i:
            print(True)
            found = True
            break
        else:
            print(False)
            found = True
            break

if not found:
    print(False)