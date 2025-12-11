s = "PPPPPP@PPP@PP$PP"
new_s = s.replace("$","@")
print(new_s)
x =new_s.split("@")
print(x)
print((len(max(x))) +1 )