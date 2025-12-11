x = input()
check = ['H', 'Q', '9']

if any(c in check for c in x):
    print("YES")
else:
    print("NO")