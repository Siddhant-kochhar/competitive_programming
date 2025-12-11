board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

res = []

row , col = len(board), len(board[0])

for r in range(row):
    row_ok = True
    curr = []
    for c in range(col):
        if board[r][c] != ".":
            if board[r][c] in curr:
                print("False")
                row_ok = False
                break
            curr.append(board[r][c])
        if c == col-1:
            res.append(curr.copy())
    
    if row_ok:
        col_ok = True
        curr_two = []
        for c in range(col):
            if board[c][r] != ".":
                if board[c][r] in curr_two:
                    print("False")
                    col_ok = False
                    break
                curr_two.append(board[c][r])
        res.append(curr_two.copy())

if row_ok and col_ok:
    print("Valid Sudoku")