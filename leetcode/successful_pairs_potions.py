spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7


if len(spells) > len(potions):
    res = [0] * len(potions)
    spells.sort()
    
    for i,j in enumerate(potions):
        low = 0 
        high = len(spells) - 1        
        while low <= high:
            mid = (low + high)//2
            if spells[mid]*j > success:
                high = mid - 1  
            else:
                low = mid + 1
        res[i] = len(spells) - low 
else:
    res = [0] * len(spells)
    potions.sort()
    
    for i,j in enumerate(spells):
        low = 0 
        high = len(potions) - 1         
        while low <= high:
            mid = (low + high)//2
            if potions[mid]*j > success:
                high = mid - 1  
            else:
                low = mid + 1
        res[i] = len(potions) - low 
print(res)




