n = 10 
initial = 1  
curr = 1     
res = 0       

for i in range(1, n + 1):
    if i % 7 == 1 and i != 1: 
        initial += 1           
        curr = initial         
    res += curr                
    curr += 1                  

print(res)