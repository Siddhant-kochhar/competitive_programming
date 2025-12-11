'''
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
'''

people = [1,2]
limit = 3

left = 0 
right = len(people) - 1
people.sort()
res = 0

while left <= right:
    if people[left] + people[right] <= limit:
        left += 1
    right -= 1
    res += 1

print(res)