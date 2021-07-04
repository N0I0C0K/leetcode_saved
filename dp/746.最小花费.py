from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)+1
        dp = [0]*n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = min(dp[i-1],dp[i-2])
            if i!=len(cost):
                dp[i]+=cost[i]
        return dp[len(cost)]

a = Solution()
print(a.minCostClimbingStairs( [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
