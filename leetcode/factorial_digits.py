n = 5

fact = 1 
while n > 1:
    fact *= n 
    n -= 1

res = [int(i) for i in str(fact)]
print(res)