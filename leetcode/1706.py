from typing import *


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = [-1]*n
        for i in range(n):
            col = i
            for row in grid:
                d = row[col]
                col += d
                if col < 0 or col >= n or row[col] != d:
                    break
            else:
                ans[i] = col
        return ans
