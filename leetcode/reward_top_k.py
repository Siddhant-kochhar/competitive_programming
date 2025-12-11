'''
Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
Output: [1,2]
Explanation: 
Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
'''

from collections import defaultdict
import heapq

positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is studious","the student is smart"]
student_id = [1,2]
k = 2

marks = defaultdict(int)

for i,j in enumerate(report):
    for positive in positive_feedback:
        if positive in j:
            marks[student_id[i]] += 3 
    for negative in negative_feedback:
        if negative in j:
            marks[student_id[i]] -= 1 

max_heap = [(-value, key) for key, value in marks.items()]
heapq.heapify(max_heap)


res = []
for w in range(k):
    z,t = heapq.heappop(max_heap)
    res.append(t)

print(res)
    