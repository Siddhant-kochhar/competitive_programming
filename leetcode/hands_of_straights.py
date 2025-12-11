'''
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
'''

from collections import Counter
import heapq

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

if len(hand)%groupSize:
    return(False)

count = Counter(hand)
minH = list(count.keys())
heapq.heapify(minH)
while minH:
    first = minH[0]

    for i in range(first,first+groupSize):
        if i not in count:
            return False
        count[i] -= 1 
        if count[i] ==0:
            if i != minH[0]:
                return False
            heapq.heapop(minH)
return True
    

    