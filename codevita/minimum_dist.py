from collections import defaultdict, deque

# ------------------ Utility Functions ------------------

def extract_points(x1, y1, x2, y2):
    """Return all integer coordinate points on the given segment"""
    pts = []
    dx, dy = x2 - x1, y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return [(x1, y1)]
    for i in range(steps + 1):
        x = round(x1 + i * dx / steps)
        y = round(y1 + i * dy / steps)
        pts.append((x, y))
    return pts


def rotate_clockwise(cx, cy, px, py):
    """Rotate a point 90 degrees clockwise around a center"""
    rel_x, rel_y = px - cx, py - cy
    return (cx + rel_y, cy - rel_x)


def chebyshev_dist(a, b):
    """Return Chebyshev distance between two points"""
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


# ------------------ Step 1: Identify Stars ------------------

def identify_nodes(segments):
    """Detect intersection nodes (star centers) where ≥ 2 segments meet"""
    point_map = defaultdict(set)
    for idx, (x1, y1, x2, y2) in enumerate(segments):
        for pt in extract_points(x1, y1, x2, y2):
            point_map[pt].add(idx)

    node_map = {}
    for pt, connected in point_map.items():
        if len(connected) >= 2:
            node_map[pt] = list(connected)
    return node_map



def gather_reachable(center, segments, seg_ids, limit=150):
    """Find all points reachable by rotating around the given star center"""
    cx, cy = center
    reachable = {center}

    for sid in seg_ids:
        x1, y1, x2, y2 = segments[sid]
        pts = extract_points(x1, y1, x2, y2)

        for px, py in pts:
            if (px, py) == center:
                continue
            reachable.add((px, py))

            cur_x, cur_y = px, py
            # Rotate 3 times (90° each) to simulate full rotation
            for _ in range(3):
                cur_x, cur_y = rotate_clockwise(cx, cy, cur_x, cur_y)
                if -limit <= cur_x <= limit and -limit <= cur_y <= limit:
                    reachable.add((cur_x, cur_y))
    return reachable



def compute_min_stars(node_reach, start, end):
    """Compute minimum number of stars required to reach the destination"""
    start_nodes = [n for n, r in node_reach.items() if start in r]
    if not start_nodes:
        return None

    # Direct reach check
    for n in start_nodes:
        if end in node_reach[n]:
            return 1

    # Build adjacency between stars that overlap
    graph = defaultdict(list)
    all_nodes = list(node_reach.keys())

    for i in range(len(all_nodes)):
        for j in range(i + 1, len(all_nodes)):
            if node_reach[all_nodes[i]] & node_reach[all_nodes[j]]:
                graph[all_nodes[i]].append(all_nodes[j])
                graph[all_nodes[j]].append(all_nodes[i])

    # BFS traversal for minimum star transitions
    queue = deque()
    visited = set()

    for s in start_nodes:
        queue.append((s, 1))  # (node, count)
        visited.add(s)

    while queue:
        node, hops = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                if end in node_reach[nxt]:
                    return hops + 1
                visited.add(nxt)
                queue.append((nxt, hops + 1))
    return None




def compute_min_shift(node_reach, end):
    """If destination not reachable, compute minimum grid shift required"""
    min_d = float('inf')
    for reachable in node_reach.values():
        for pt in reachable:
            min_d = min(min_d, chebyshev_dist(pt, end))
    return int(min_d if min_d != float('inf') else 0)




def main():
    num_segments = int(input().strip())
    segments = [tuple(map(int, input().split())) for _ in range(num_segments)]

    start_pt = tuple(map(int, input().split()))
    end_pt = tuple(map(int, input().split()))

    nodes = identify_nodes(segments)

    # If no stars exist, output direct Chebyshev distance
    if not nodes:
        print(chebyshev_dist(start_pt, end_pt))
        return

    node_reach = {n: gather_reachable(n, segments, ids) for n, ids in nodes.items()}

    res = compute_min_stars(node_reach, start_pt, end_pt)
    if res is not None:
        print(res)
    else:
        print(compute_min_shift(node_reach, end_pt))



if __name__ == "__main__":
    main()