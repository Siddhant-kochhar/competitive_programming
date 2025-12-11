x = [0, 2, 1, 0]
n = len(x)

if n < 3:
    print("False")
else:
    i = 0
    
    while i + 1 < n and x[i] < x[i + 1]:
        i += 1
    
    if i == 0 or i == n - 1:
        print("False")
    else:
        # Walk down
        while i + 1 < n and x[i] > x[i + 1]:
            i += 1
        print("True" if i == n - 1 else "False")
