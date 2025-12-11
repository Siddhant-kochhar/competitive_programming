'''
Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
'''
skill = [3,2,5,1,3,4]

n = len(skill)
total = sum(skill)
target = total // (n//2)   

res = []      
pairs = []    

for i in skill:
    x = target - i
    if x in res:
        pairs.append((x, i))   
        res.remove(x)          
    else:
        res.append(i)         

print("Pairs:", pairs)


chemistry = sum(a*b for a, b in pairs)
print("Chemistry:", chemistry)
