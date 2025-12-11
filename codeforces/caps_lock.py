x = input()

if x.isupper():
    print(x.lower())
elif x[0].islower() and x[1:].isupper():
    print(x[0].upper() + x[1:].lower())
else:
    print(x)
