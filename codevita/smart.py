import sys
import math
from collections import defaultdict

EPS = 1e-6

def round2(x):
    return round(x, 2)

def point_key(x, y):
    return (round2(x), round2(y))

def seg_len(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.hypot(x1 - x2, y1 - y2)

def segment(a, b, p):
    # check if point p lies on segment ab
    (x1, y1), (x2, y2), (x, y) = (a, b, p)
    cross = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
    if abs(cross) > EPS:
        return False
    dot = (x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)
    if dot < -EPS:
        return False
    sq_len = (x2 - x1)**2 + (y2 - y1)**2
    if dot - sq_len > EPS:
        return False
    return True

def intersection(a1, a2, b1, b2):
    # compute intersection points (with high precision)
    (x1, y1) = a1
    (x2, y2) = a2
    (x3, y3) = b1
    (x4, y4) = b2
    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    pts = []
    if abs(denom) > EPS:
        px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
        py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
        p = (px, py)
        if segment(a1, a2, p) and segment(b1, b2, p):
            pts.append(point_key(px, py))
    else:
        # check collinear overlap
        area = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
        if abs(area) > EPS:
            return []
        for p in [b1, b2]:
            if segment(a1, a2, p):
                pts.append(point_key(p[0], p[1]))
        for p in [a1, a2]:
            if segment(b1, b2, p):
                pts.append(point_key(p[0], p[1]))
        pts = list(dict.fromkeys(pts))  # remove duplicates
    return pts

def area(points):
    n = len(points)
    if n < 3:
        return 0.0
    s = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]
        s += x1*y2 - x2*y1
    return abs(s) / 2.0

def perimeter(points):
    n = len(points)
    s = 0.0
    for i in range(n):
        s += seg_len(points[i], points[(i+1) % n])
    return s

def build_faces(points, adj):
    neigh_sorted = {}
    for u in adj:
        nbrs = list(dict.fromkeys(adj[u]))
        nbrs.sort(key=lambda v: math.atan2(points[v][1]-points[u][1], points[v][0]-points[u][0]))
        neigh_sorted[u] = nbrs

    next_edge = {}
    for v in neigh_sorted:
        lst = neigh_sorted[v]
        m = len(lst)
        idx = {lst[i]: i for i in range(m)}
        for i, u in enumerate(lst):
            prev_idx = (idx[u] - 1) % m
            w = lst[prev_idx]
            next_edge[(u, v)] = (v, w)

    visited = set()
    faces = []
    for u in neigh_sorted:
        for v in neigh_sorted[u]:
            if (u, v) in visited:
                continue
            cycle = []
            cur = (u, v)
            while True:
                if cur in visited:
                    break
                visited.add(cur)
                cycle.append(cur[0])
                cur = next_edge.get(cur)
                if cur is None:
                    cycle = []
                    break
                if cur[0] == u and cur[1] == v:
                    break
            if len(cycle) >= 3:
                faces.append(cycle)
    # remove duplicates
    uniq = []
    seen = set()
    for f in faces:
        t = tuple(f)
        if t not in seen:
            seen.add(t)
            uniq.append(f)
    return uniq

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    segs = []
    total_length = 0.0

    for _ in range(n):
        x1 = float(next(it)); y1 = float(next(it))
        x2 = float(next(it)); y2 = float(next(it))
        a = (x1, y1); b = (x2, y2)
        segs.append((a, b))
        total_length += seg_len(a, b)

    # Step 1: collect intersection points
    points_set = set()
    seg_points = [set() for _ in range(n)]
    for i, (a, b) in enumerate(segs):
        pa = point_key(a[0], a[1])
        pb = point_key(b[0], b[1])
        points_set.update([pa, pb])
        seg_points[i].update([pa, pb])

    for i in range(n):
        a1, a2 = segs[i]
        for j in range(i+1, n):
            b1, b2 = segs[j]
            inters = intersection(a1, a2, b1, b2)
            for p in inters:
                points_set.add(p)
                seg_points[i].add(p)
                seg_points[j].add(p)

    points = sorted(list(points_set))
    idx_of = {p: i for i, p in enumerate(points)}

    adj = defaultdict(list)
    edge_set = set()
    for i, (a, b) in enumerate(segs):
        pts_on = list(seg_points[i])
        def param(p):
            dx = b[0]-a[0]; dy = b[1]-a[1]
            if abs(dx) >= abs(dy):
                if abs(dx) < EPS: return 0.0
                return (p[0]-a[0]) / dx
            else:
                if abs(dy) < EPS: return 0.0
                return (p[1]-a[1]) / dy
        pts_on.sort(key=param)
        for k in range(len(pts_on)-1):
            u = idx_of[pts_on[k]]
            v = idx_of[pts_on[k+1]]
            if u == v:
                continue
            a_pt = points[u]; b_pt = points[v]
            if seg_len(a_pt, b_pt) < EPS:
                continue
            if (u, v) in edge_set or (v, u) in edge_set:
                continue
            edge_set.add((u, v)); edge_set.add((v, u))
            adj[u].append(v)
            adj[v].append(u)

    if not adj:
        print("Abandoned")
        return

    faces_idx = build_faces(points, adj)
    if not faces_idx:
        print("Abandoned")
        return

    # compute areas of faces
    faces_with_area = []
    for fi in faces_idx:
        poly = [points[i] for i in fi]
        a = area(poly)
        if a > EPS:
            faces_with_area.append((a, fi))

    if not faces_with_area:
        print("Abandoned")
        return

    faces_with_area.sort(reverse=True, key=lambda x: x[0])

    # ignore outermost infinite face (largest one)
    if len(faces_with_area) > 1:
        best_area = faces_with_area[1][0]
        best_pts = [points[i] for i in faces_with_area[1][1]]
    else:
        best_area = faces_with_area[0][0]
        best_pts = [points[i] for i in faces_with_area[0][1]]

    if best_area < EPS:
        print("Abandoned")
        return

    perim = perimeter(best_pts)
    leftover = total_length - perim
    if leftover < EPS:
        print("Kalyan")
        return

    # Assuming computer makes square of leftover length
    comp_area = (leftover * leftover) / 16.0

    if comp_area > best_area + EPS:
        print("Computer")
    else:
        print("Kalyan")


if __name__ == "__main__":
    main()