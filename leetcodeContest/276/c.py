from typing import *


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            temp = questions[i]
            j = i+temp[1]+1
            dp[i] = max(dp[i+1], temp[0]+(dp[j] if j < n else 0))
        return dp[0]


a = Solution()
print(a.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
