'''
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

'''

image = [[1,2,3],[4,5,6],[7,8,9]]
sr=0
sc=0
color=10

row ,col = len(image), len(image[0])

queue = [(sr, sc)]
visitedset = set((sr, sc))
directions = ((0,1),(0,-1),(1,0),(-1,0))
original_color = image[sr][sc]
image[sr][sc] = color

while queue:
    r,c = queue.pop(0)
    for dr,dc in directions:
        nr,nc = r+dr,c+dc
        if 0<=nr<row and 0<=nc<col:
            if (nr,nc) not in visitedset and image[nr][nc] == original_color:
                image[nr][nc] = color
                queue.append((nr,nc))
                visitedset.add((nr,nc))
            else:
                continue

print(image)