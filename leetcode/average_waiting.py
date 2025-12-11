customers = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]

prep = 0

waiting = []

for i,j in customers:
    if i >= prep:
        prep = i 
        waiting.append(j)
        prep += j
    else:
        waiting.append(abs(prep-i))
        waiting.append(j)
        prep += j 

print(sum(waiting)/len(customers))
