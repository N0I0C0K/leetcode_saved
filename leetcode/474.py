# 474. 一和零   https://leetcode-cn.com/problems/ones-and-zeroes/
# 
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m,zeros-1,-1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]

a = Solution()
print(a.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))