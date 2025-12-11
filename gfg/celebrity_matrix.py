mat = [[1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]]

row , col = len(mat), len(mat[0])

celebrity_found = False
for r in range(row):
    row_ok = True
    for c in range(col):
        if mat[r][c] == 1 and r != c:
            row_ok = False
            break
    
    if row_ok:
        col_ok = True
        for c in range(col):
            if mat[c][r] == 0 and c != r:
                col_ok = False
                break
        
        if col_ok:
            print(r)
            celebrity_found = True

if not celebrity_found:
    print(-1)