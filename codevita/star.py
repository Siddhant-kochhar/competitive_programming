from collections import defaultdict, deque

def find_center(lines):
    """Find centers where 2+ lines intersect"""
    point_to_lines = defaultdict(set)
    for i, (x1, y1, x2, y2) in enumerate(lines):
        for pt in get_points(x1, y1, x2, y2):
            point_to_lines[pt].add(i)
    centers = {}
    for pt, line_set in point_to_lines.items():
        if len(line_set) >= 2:
            centers[pt] = list(line_set)
    return centers

def get_rechable(center, lines, line_indices, max_coord=150):
    """Get all points reachable from a star center through any rotation"""
    cx, cy = center
    reachable = {center}
    for idx in line_indices:
        x1, y1, x2, y2 = lines[idx]
        points = get_points(x1, y1, x2, y2)
        for px, py in points:
            if (px, py) == center:
                continue
            reachable.add((px, py))
            curr_x, curr_y = px, py
            for _ in range(3):
                curr_x, curr_y = rotate_90(cx, cy, curr_x, curr_y)
                if -max_coord <= curr_x <= max_coord and -max_coord <= curr_y <= max_coord:
                    reachable.add((curr_x, curr_y))
    return reachable

def get_points(x1, y1, x2, y2):
    """Get all integer points on a line segment"""
    points = []
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    
    if steps == 0:
        return [(x1, y1)]
    
    for i in range(steps + 1):
        x = round(x1 + i * dx / steps)
        y = round(y1 + i * dy / steps)
        points.append((x, y))
    
    return points



def rotate_90(cx, cy, px, py):
    """Rotate point (px, py) 90 degrees clockwise around (cx, cy)"""
    rel_x, rel_y = px - cx, py - cy
    return (cx + rel_y, cy - rel_x)



def distance(p1, p2):
    return max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))

def find_min_stars(centers, star_reach, source, destination):
    # Identify stars that can reach source
    source_stars = [c for c, r in star_reach.items() if source in r]
    if not source_stars:
        return None
    
    # If destination reachable within one star
    for s in source_stars:
        if destination in star_reach[s]:
            return 1

    # Build adjacency: stars are connected if their reachable sets overlap
    adj = defaultdict(list)
    stars = list(star_reach.keys())
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            if star_reach[stars[i]] & star_reach[stars[j]]:
                adj[stars[i]].append(stars[j])
                adj[stars[j]].append(stars[i])

    # BFS over stars
    queue = deque()
    visited = set()
    for s in source_stars:
        queue.append((s, 1))  # 1 star used so far
        visited.add(s)
    
    while queue:
        star, count = queue.popleft()
        for nxt in adj[star]:
            if nxt not in visited:
                if destination in star_reach[nxt]:
                    return count + 1
                visited.add(nxt)
                queue.append((nxt, count + 1))
    return None

def find_min_shift(star_reach, destination):
    min_dist = float('inf')
    for pts in star_reach.values():
        for p in pts:
            min_dist = min(min_dist, distance(p, destination))
    return min_dist if min_dist != float('inf') else 0


n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
source = tuple(map(int, input().split()))
destination = tuple(map(int, input().split()))

centers = find_center(lines)

if not centers:
    print(distance(source, destination))
else:
    star_reach = {c: get_rechable(c, lines, idxs) for c, idxs in centers.items()}
    result = find_min_stars(centers, star_reach, source, destination)
    if result is not None:
        print(result)
    else:
        print(find_min_shift(star_reach, destination))
