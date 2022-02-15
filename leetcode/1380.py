from typing import *


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans: List[int] = []
        n, m = len(matrix), len(matrix[0])
        for row in matrix:
            m = min(enumerate(row), key=lambda x: (x[1], x[0]))
            for i in range(0, n):
                if m[1] < matrix[i][m[0]]:
                    break
            else:
                ans.append(m[1])
        return ans


a = Solution()
print(a.luckyNumbers([[7, 8], [1, 2]]))
