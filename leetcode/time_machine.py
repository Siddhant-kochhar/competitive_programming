'''
A == B # 0 COSTING
A > B # 2 COSTING 
A < B # 1 COSTING 
'''

years = [2000,2021,2005]

res = 0 
for i in range(1,len(years)):
   
    if years[i] < years[i - 1]:
        res +=2
       
    elif years[i] > years[i -1]:
        res += 1
       
    else:
        res += 0 
    

print(res)
    