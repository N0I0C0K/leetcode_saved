from typing import *
from collections import deque


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = [False]*n
        vis[0] = True
        q = deque([0])
        ans, dist = 0, 1
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if vis[v]:
                        continue
                    vis[v] = True
                    q.append(v)
                    ans = max(ans, (dist*2-1) //
                              patience[v]*patience[v]+2*dist+1)
            dist += 1
        return ans
