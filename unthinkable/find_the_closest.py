x = [8, 4, 1, 3, 6]
element = 5 

diff = []
for i in range(len(x)):
    diff.append(abs(element - x[i]))  

minimum = min(diff)
temp = []
    
for i in range(len(diff)):
    if diff[i] == minimum:
        temp.append(x[i])  

print(max(temp))  