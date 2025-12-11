from collections import deque

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]

rows = len(grid)
cols = len(grid[0])
start  = deque([(0,0)])

res = 0 


directions = [(1,1)]

while start:
    for dr,dc in directions:
        x,y = start.popleft()
        res += grid[x][y]
        if 0< x + dr < rows and 0 <y+dc < cols:
            start.append((x + dr,y+dc))



end = deque([(0, cols-1)])
right = 0 
directions = [(1, -1)]

while end:
    for dr, dc in directions:
        x, y = end.popleft()
        right += grid[x][y]
        if 0 <= x + dr < rows and 0 <= y + dc < cols:
            end.append((x + dr, y + dc))


print(res)
print(right)
    
