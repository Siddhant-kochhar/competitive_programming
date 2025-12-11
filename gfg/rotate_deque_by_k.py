dq = [1, 2, 3, 4, 5, 6]
type = 1
k = 2

print(dq[:-k+1])
print(dq[-k+1:])
print()
def rotate(dq,type,k):
    if type == 1:
        return dq[-k:] + dq[:-k]
    else:
        return dq[-k+1:] + dq[:-k+1]
    
print(rotate(dq,type,k))