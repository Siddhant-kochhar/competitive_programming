'''
grid[][] = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]
Output: 4
'''
from collections import deque

grid = [['L', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']]

rows = len(grid)
cols = len(grid[0])
count = 0 

visited = set()  # Use only one visited set
lands = deque()

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "L" and (i,j) not in visited:
            lands.append((i,j))

while lands:
    start_x, start_y = lands.popleft()
    
    if (start_x, start_y) not in visited:  
        visited.add((start_x, start_y))
        neighbours = deque([(start_x, start_y)]) 
        directions = [(-1,-1), (-1,0), (-1,1),(0,-1),(0,1),(1,-1), (1,0), (1,1)]# Move directions outside inner loop
        
        while neighbours:
            x, y = neighbours.popleft()
            
            for dr,dc in directions:
                new_dr, new_dc = x + dr, y + dc
                if 0 <= new_dr < rows and 0 <= new_dc < cols:
                    if grid[new_dr][new_dc] == "L" and (new_dr, new_dc) not in visited:
                        visited.add((new_dr, new_dc))
                        neighbours.append((new_dr, new_dc))
        
        count += 1  

print(count)  