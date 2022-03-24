from typing import *


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                nums, a = 0, 0
                for x, y in ((i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)):
                    if 0 <= x < n and 0 <= y < m:
                        nums += 1
                        a += img[x][y]
                res[i][j] = int(a/nums)
        return res
