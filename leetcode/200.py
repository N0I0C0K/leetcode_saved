from typing import *
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = [[False for _ in grid[0]] for k in grid]
        n, m = len(grid), len(grid[0])

        def bfs(x, y):
            nonlocal vis
            que: Deque[Tuple[int, int]] = deque()
            que.append((x, y))
            while len(que) > 0:
                x, y = que.popleft()
                if x < 0 or x >= n or y < 0 or y >= m or vis[x][y]:
                    continue
                vis[x][y] = True
                if grid[x][y] == '1':
                    for item in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                        que.append(item)
        ans = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == '1' and not vis[i][j]:
                    ans += 1
                    bfs(i, j)
        return ans


a = Solution()
print(a.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
