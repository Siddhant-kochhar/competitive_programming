'''
Example 1:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Hence, answer = [10,55,45,25,25]


Example 2:
Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]
'''
from collections import defaultdict

bookings = [[2,2,35],[1,2,10]]
n = 2

total_flight = defaultdict(0)

for i in bookings:
    src_one,src_two,flight = i 
    for t in range(src_one,src_two+1):
        total_flight[t]+= (flight)
print(total_flight)

total_flight = dict(sorted(total_flight.items(), key = lambda x:x[0]))
res = [0]*n
for key,value in total_flight.items():
    res[key-1]= (value)

print(res)