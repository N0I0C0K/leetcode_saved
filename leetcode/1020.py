from typing import *
from collections import deque


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[False for _ in grid[0]] for _k in grid]
        que: Deque[Tuple[int, int]] = deque()
        for i in range(n):
            que.append((i, 0))
            que.append((i, m-1))
        for i in range(m):
            que.append((0, i))
            que.append((n-1, i))
        while len(que) > 0:
            x, y = que.popleft()
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if grid[x][y] == 0 or vis[x][y]:
                continue
            vis[x][y] = True
            for item in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                que.append(item)
        ans = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1 and not vis[i][j]:
                    ans += 1
        return ans


a = Solution()
print(a.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
