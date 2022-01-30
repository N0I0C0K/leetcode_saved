from typing import *
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[water-1 for water in row] for row in isWater]
        que = deque((i, j) for i, row in enumerate(isWater)
                    for j, water in enumerate(row) if water)
        while len(que) > 0:
            i, j = que.popleft()
            for x, y in ((i-1, j), (i+1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j]+1
                    que.append((x, y))
        return ans


a = Solution()
print(a.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
