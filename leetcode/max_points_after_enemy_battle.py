'''
Input: enemyEnergies = [3,2,2], currentEnergy = 2
Output: 3
'''

enemyEnergies = [3,2,2]
currentEnergy = 2

enemyEnergies.sort()
print(enemyEnergies)

l = 0
r = len(enemyEnergies) - 1
points = 0
maxPoints = 0

while l <= r:
    if currentEnergy >= enemyEnergies[l]:   
        currentEnergy -= enemyEnergies[l]
        points += 1
        l += 1
        maxPoints = max(maxPoints, points)   
    elif points > 0:                       
        currentEnergy += enemyEnergies[r]
        points -= 1
        r -= 1
    else:                                   
        break

print(maxPoints)
