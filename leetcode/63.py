from typing import *
from collections import deque


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        vis = [[False for i in range(m+1)] for j in range(n+1)]
        que: Deque[Tuple[int, int]] = deque()
        dp[0][1] = 1
        que.append((1, 1))
        while que:
            x, y = que.popleft()
            if x > n or y > m or vis[x][y]:
                continue
            vis[x][y] = True
            if obstacleGrid[x-1][y-1] == 1:
                dp[x][y] = 0
                continue
            dp[x][y] = dp[x-1][y]+dp[x][y-1]
            for xt, yt in ((x+1, y), (x, y+1)):
                que.append((xt, yt))
        return dp[n][m]


a = Solution()
print(a.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
