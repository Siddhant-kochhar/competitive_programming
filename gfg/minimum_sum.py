'''
Input: arr[] = [6, 8, 4, 5, 2, 3]
Output: "604"
Explanation: The minimum sum is formed by numbers 358 and 246.
'''

import heapq 

arr = [5, 3, 0, 7, 4]

heapq.heapify(arr)

num1 = ""
num2 = ""

flag = True
while arr:
    if flag:
        num1 += str(heapq.heappop(arr))
        flag = False
    else:
        num2 += str(heapq.heappop(arr))
        flag = True
    
print(num1)
print(num2)

print(str(int(num1)+int(num2)))

