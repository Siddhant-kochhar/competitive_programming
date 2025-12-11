'''
x = [1, 1, 0
    -1, 1, 1
    -1, 1, -1]

    1 --> rat
    0 --> egg
   -1 --> nothing
'''

matrix = [[1, 1, 0],
          [-1, 1, 1],
          [-1, 1, -1]]

rows = len(matrix)
cols = len(matrix[0]) 
rat_count = 0 
can_eat = 0 

for i in range(rows):
    for j in range(0, cols):
        if matrix[i][j] == 1:
            rat_count += 1
print(rat_count)

queue = [(0,0)]
while queue:
    directions = [(0,1),(-1,0),(0,-1),(1,0)]
    for direction in directions:
        new_x = queue[0][0] + direction[0]
        new_y = queue[0][1] + direction[1]
        if 0 <= new_x < rows and 0 <= new_y < cols:
            if matrix[new_x][new_y] == 1:
                can_eat += 1
                rat_count -= 1
            queue.append((new_x, new_y))
    queue.pop(0)
print(can_eat)


