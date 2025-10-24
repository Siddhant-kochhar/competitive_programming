import heapq
import math

class Solution:
    def kClosest(self, points, k):
        # code here
        origin = [0,0]
        
        res = []
        maxheap = []
        
        for (x,y) in points:
            dist = math.sqrt((x - origin[0])**2 + (y - origin[1])**2)
            heapq.heappush(maxheap, (dist, [x,y]))
            
        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        
        return (res)
                