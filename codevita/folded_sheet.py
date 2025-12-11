def sheet(R, C, instructions):
   
    sheet = [[[r * C + c + 1] for c in range(C)] for r in range(R)]

    for j in instructions:
        if not j:
            continue
        typ = j[0]      
        idx = int(j[1:]) 

        if typ == 'v':  # Vertical fold (right part over left)
            left = idx
            rows, cols = len(sheet), len(sheet[0])
            right = cols - left
            new_cols = max(left, right)
            new_sheet = [[[] for _ in range(new_cols)] for _ in range(rows)]

            
            for r in range(rows):
                for c in range(left):
                    new_c = new_cols - (left - c)
                    if 0 <= new_c < new_cols:
                        new_sheet[r][new_c] = list(sheet[r][c])

            
            for r in range(rows):
                for c in range(right):
                    new_c = new_cols - 1 - c
                    if 0 <= new_c < new_cols and left + c < cols:
                        new_sheet[r][new_c].extend(reversed(sheet[r][left + c]))
            sheet = new_sheet

        elif typ == 'h':  
            top = idx
            rows, cols = len(sheet), len(sheet[0])
            bottom = rows - top
            new_rows = max(top, bottom)
            new_sheet = [[[] for _ in range(cols)] for _ in range(new_rows)]

            # Copy top part
            for r in range(top):
                new_r = new_rows - (top - r)
                if 0 <= new_r < new_rows:
                    for c in range(cols):
                        new_sheet[new_r][c] = list(sheet[r][c])

            # Fold bottom part over
            for r in range(bottom):
                new_r = new_rows - 1 - r
                if 0 <= new_r < new_rows and top + r < rows:
                    for c in range(cols):
                        new_sheet[new_r][c].extend(reversed(sheet[top + r][c]))
            sheet = new_sheet

   
    top_cell = bottom_cell = None
    for r in range(len(sheet)):
        for c in range(len(sheet[0])):
            if sheet[r][c]:
                top_cell = sheet[r][c][-1]
                bottom_cell = sheet[r][c][0]

    return top_cell, bottom_cell


if __name__ == "__main__":
    R, C = map(int, input().split())
    instructions = input().split()
    top, bottom = sheet(R, C, instructions)
    print(f"{top} {bottom}", end="")
