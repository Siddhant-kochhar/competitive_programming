'''
Input: s = "abbccc", k = 2
Output: 6
Explaination: We remove two 'c' to get the value as 12 + 22 + 12 = 6 
or We remove one 'b' and one 'c' to get the value 12 + 12 + 22 = 6.
'''

from collections import Counter
import heapq

s = "aaab"
k = 2

s_dict = Counter(s)

max_heap = [(-value, key) for key, value in s_dict.items()]

heapq.heapify(max_heap)

for j in range(k):
    x,y = heapq.heappop(max_heap)
    if x + 1 <0:
        heapq.heappush((max_heap),(x+1,y))

res = 0
for z,t in max_heap:
    print(z,t)
    res += abs(z)**2
print(res)
