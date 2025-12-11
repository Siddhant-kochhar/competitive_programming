from collections import deque

def solve_ladder_problem():
    # Read input
    line = input().strip()
    m, n = map(int, line.split())
    
    grid = []
    for _ in range(m):
        row = input().strip()
        if ' ' in row:
            grid.append(row.split())
        else:
            grid.append(list(row))
    
    # Find ladder cells
    source_cells = []
    dest_cells = []
    
    for i in range(m):
        for j in range(len(grid[i])):
            if grid[i][j] in ['l', 'I', 'i']:
                source_cells.append((i, j))
            elif grid[i][j] == 'L':
                dest_cells.append((i, j))
    
    if not source_cells or not dest_cells:
        print("Impossible")
        return
    
    source_cells.sort()
    dest_cells.sort()
    ladder_len = len(source_cells)

    # Validate destination cells: must form a straight contiguous line of same length
    if len(dest_cells) != ladder_len:
        print("Impossible")
        return
    # confirm dest contiguous and straight
    def is_contiguous_line(cells):
        if not cells:
            return False
        rows = {r for r, _ in cells}
        cols = {c for _, c in cells}
        if len(rows) == 1:
            r = next(iter(rows))
            sorted_cols = sorted(c for _, c in cells)
            return all(sorted_cols[i] + 1 == sorted_cols[i+1] for i in range(len(sorted_cols)-1))
        if len(cols) == 1:
            c = next(iter(cols))
            sorted_rows = sorted(r for r, _ in cells)
            return all(sorted_rows[i] + 1 == sorted_rows[i+1] for i in range(len(sorted_rows)-1))
        return False
    if not is_contiguous_line(dest_cells):
        print("Impossible")
        return
    
    # Determine orientations
    start_orient = 0 if source_cells[0][0] == source_cells[-1][0] else 1
    dest_orient = 0 if dest_cells[0][0] == dest_cells[-1][0] else 1
    
    start_pos = source_cells[0]
    dest_pos = dest_cells[0]
    
    # BFS
    queue = deque([(start_pos[0], start_pos[1], start_orient, 0)])
    visited = set()
    visited.add((start_pos[0], start_pos[1], start_orient))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def can_place(r, c, orient):
        """Check if ladder can be placed at (r,c) with given orientation"""
        if orient == 0:  # horizontal
            if r < 0 or r >= m or c < 0 or c + ladder_len > n:
                return False
            for j in range(ladder_len):
                if grid[r][c + j] == 'B':
                    return False
        else:  # vertical
            if r < 0 or r + ladder_len > m or c < 0 or c >= n:
                return False
            for i in range(ladder_len):
                if grid[r + i][c] == 'B':
                    return False
        return True
    
    def can_rotate(r, c, curr_orient):
        """Check if rotation is possible at (r,c).
        Use a stricter model: require a ladder_len x ladder_len square clearance around pivot.
        The pivot is taken as (r,c), i.e., top-left of the current placement.
        """
        # Determine square bounds from (r,c) to (r+L-1, c+L-1)
        r2 = r + ladder_len - 1
        c2 = c + ladder_len - 1
        if r < 0 or c < 0 or r2 >= m or c2 >= n:
            return False
        for rr in range(r, r2 + 1):
            for cc in range(c, c2 + 1):
                if grid[rr][cc] == 'B':
                    return False
        return True
    
    # Precompute destination set for exact match check
    dest_set = set(dest_cells)

    while queue:
        r, c, orient, steps = queue.popleft()
        
        # Check goal: ladder must exactly cover destination cells
        if orient == 0:
            occ = {(r, c + j) for j in range(ladder_len)}
        else:
            occ = {(r + i, c) for i in range(ladder_len)}
        if occ == dest_set and orient == dest_orient:
            print(steps)
            return
        
        # Try 4 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if can_place(nr, nc, orient):
                state = (nr, nc, orient)
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, orient, steps + 1))
        
        # Try rotation
        if can_rotate(r, c, orient):
            new_orient = 1 - orient
            if can_place(r, c, new_orient):
                state = (r, c, new_orient)
                if state not in visited:
                    visited.add(state)
                    queue.append((r, c, new_orient, steps + 1))
    
    print("Impossible")

solve_ladder_problem()