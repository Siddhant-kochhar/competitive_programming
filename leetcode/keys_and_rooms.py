'''
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
'''
rooms = [[2], [], [1]]
keys = {i: False for i in range(len(rooms))}
print(keys)
keys[0] = True
print(keys)

def check(rooms):
    changed = True
    while changed:
        changed = False
        for i in range(len(rooms)):
            if keys[i]:
                for j in rooms[i]:
                    if not keys[j]:
                        keys[j] = True
                        changed = True
    return all(keys.values())
print(check(rooms))
