'''
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
'''

mat = [[1,2,3],[4,5,6],[7,8,9]]

def findDiagonalOrder(mat):
    if not mat:
        return 0 
    rows , cols = len(mat), len(mat[0])

    flag = True

    up_directions = [(0, 1), (-1, 0)]
    down_directions = [(1, 0), (0, -1)]

    result = []
    r ,c = 0, 0

    while True:
        if flag:
            for dx,dy in up_directions:
                new_x, new_y = r + dx, c + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    r, c = new_x, new_y
                else:
                    r, c = r, c + 1
            result.append(mat[r][c])
            flag = not flag

        else:
            for dx,dy in down_directions:
                new_x, new_y = r + dx, c + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    r, c = new_x, new_y
                else:
                    r, c = r + 1, c
            result.append(mat[r][c])
            flag = not flag


    return result

print(findDiagonalOrder(mat))