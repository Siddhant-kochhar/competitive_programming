'''
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
'''

grid = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]

rows, cols = len(grid), len(grid[0])
queue = []
visitedset = set()
directions = ((0,1),(0,-1),(1,0),(-1,0))

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 0:
            queue.append((r,c))

while queue:
    r,c = queue.pop(0)
    for dr,dc in directions:
        nr,nc = r+dr,c+dc
        if nr>=0 and nr<rows and nc>=0 and nc<cols:
            if (nr,nc) not in visitedset and grid[nr][nc] == 2147483647:
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr,nc))
                visitedset.add((nr,nc))
            else:
                continue
print(grid)