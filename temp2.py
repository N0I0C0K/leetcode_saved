from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        re = True
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                if j < m and i+j < n:
                    if matrix[j][j+i] != matrix[j-1][j+i-1]:
                        return False
        for i in range(m):
            for j in range(1, n):
                if i + j < m:
                    if matrix[j+i][j] != matrix[j+i-1][j-1]:
                        return False
        return True

a = Solution()
print(a.isToeplitzMatrix(   [[36,59,71,15,26,82,87],
                            [56,36,59,71,15,26,82],
                            [15,0,36,59,71,15,26]]))