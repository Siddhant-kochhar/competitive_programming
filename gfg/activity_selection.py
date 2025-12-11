'''
Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: A person can perform at most four activities. The maximum set of activities that can be executed is {0, 1, 3, 4}
Input: start[] = [10, 12, 20], finish[] = [20, 25, 30]
Output: 1
Explanation: A person can perform at most one activity.
Input: start[] = [1, 3, 2, 5], finish[] = [2, 4, 3, 6]
Output: 3
Explanation: A person can perform activities 0, 1 and 3.
'''
import heapq

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

activity = []

for i,j in zip(finish,start):
    activity.append((i,j))

print(activity)

heapq.heapify(activity)
cnt = 0 
last_completed = float("-inf")

while activity:
    x,y = heapq.heappop(activity)
    if y > last_completed:
        cnt +=1 
        last_completed = x

print(cnt) 