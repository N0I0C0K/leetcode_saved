from typing import *


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        childen = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p != -1:
                childen[p].append(i)
        maxn, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n-1
            for ch in childen[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxn, cnt
            if score == maxn:
                cnt += 1
            elif score > maxn:
                maxn, cnt = score, 1
            return n-size
        dfs(0)
        return cnt
