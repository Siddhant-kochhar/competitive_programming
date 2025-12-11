def isvalid(grid, r, c, n, expvalue) -> bool:
    if r <0 or c < 0 or r >= n or c >= n or grid[r][c] != expvalue:
        return False
    if expvalue == n**2 -1:
        return True
    
    ans1 = isvalid(grid,r-2,c+1,n,expvalue+1)
    ans2 = isvalid(grid,r-2,c+2,n,expvalue+1)
    ans3 = isvalid(grid,r+1,c+2,n,expvalue+1)
    ans4 = isvalid(grid,r+2,c+1,n,expvalue+1)
    ans5 = isvalid(grid,r+2,c-1,n,expvalue+1)
    ans6 = isvalid(grid,r+1,c-2,n,expvalue+1)
    ans7 = isvalid(grid,r-1,c-2,n,expvalue+1)
    ans8 = isvalid(grid,r-2,c-1,n,expvalue+1)

    return ans1 and ans2 and ans3 and ans4 and ans5 and ans6 and ans7 and ans8 