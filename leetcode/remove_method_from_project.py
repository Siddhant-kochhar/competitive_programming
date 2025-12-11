from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        edges = {i: [] for i in range(n)}
        for i, j in invocations:
            edges[i].append(j)

        suspicious = set()
        queue = deque([k])

        # BFS with visited check (prevents infinite loop / TLE)
        while queue:
            x = queue.popleft()
            if x in suspicious:
                continue
            suspicious.add(x)
            for neigh in edges[x]:
                queue.append(neigh)

        # CORRECT removability check:
        # If any safe method (a not in suspicious) calls into suspicious (b in suspicious),
        # removal is impossible -> return all methods.
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return [i for i in range(n)]

        # Otherwise it's safe to remove the whole suspicious set
        res = [i for i in range(n) if i not in suspicious]
        return res
