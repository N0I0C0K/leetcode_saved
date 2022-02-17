class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0]*n for _ in range(n)] for __ in range(k+1)]
        for step in range(k+1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            ti, tj = i+di, j+dj
                            if 0 <= ti < n and 0 <= tj < n:
                                dp[step][i][j] += dp[step-1][ti][tj]/8
        return dp[k][row][column]
