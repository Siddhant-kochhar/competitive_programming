from collections import deque

mat = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
rows, cols = len(mat), len(mat[0])

directions = [('U', -1, 0), ('D', 1, 0), ('R', 0, 1), ('L', 0, -1)]
res = []

def find_paths():
    queue = deque()
    queue.append((0, 0, ""))  # (x, y, path)
    visited = set()
    
    while queue:
        x, y, path = queue.popleft()
        
        # Check if we reached the destination
        if x == rows-1 and y == cols-1:
            res.append(path)
            continue
            
        visited.add((x, y))
        
        # Try all four directions
        for dir_name, dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check boundaries and if it's a valid cell
            if 0 <= new_x < rows and 0 <= new_y < cols:
                if mat[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, path + dir_name))
find_paths()
if res:
    print("All possible paths:", res)
    print("Shortest path:", min(res, key=len))
else:
    print("No path exists")