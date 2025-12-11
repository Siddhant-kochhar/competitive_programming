def numberOfMatches(n):
    res = 0 
    while n > 1:
        if n%2 !=0:
            res += n//2
            n = (n//2) + 1
        else:
            res += n//2
            n = n//2
            
            
        
    return res
    
print(numberOfMatches(7))