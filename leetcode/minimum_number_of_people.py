'''
Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
'''

n = 3
languages = [[2],[1,3],[1,2],[3]]
friendships = [[1,4],[1,2],[3,4],[2,3]]

known = {i:set() for i in range(1,n+2)}
print(known)

for i in range(len(languages)):
    known[i+1].update(languages[i])

print(known)
res = set()

conflict_users = set()
for x, y in friendships:
    if not (known[x] & known[y]):  
        conflict_users.add(x)
        conflict_users.add(y)
min_teach = float('inf')

for L in range(1, n+1):
    teach_count = 0
    for user in conflict_users:
        if L not in known[user]:
            teach_count += 1
    min_teach = min(min_teach, teach_count)



print(min_teach)