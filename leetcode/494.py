from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [[0]*2001 for _ in range(len(nums))]
        dp[0][1000+nums[0]] += 1
        dp[0][1000-nums[0]] += 1
        for i in range(1,len(nums)):
            for j in range(-1000, 1001):
                if dp[i-1][j+1000] > 0:
                    dp[i][j+1000+nums[i]] += dp[i-1][j+1000]
                    dp[i][j+1000-nums[i]] += dp[i-1][j+1000]
        return 0 if S > 1000 else dp[len(nums)-1][S+1000]

a = Solution()
print(a.findTargetSumWays([0,0,0,0,0,1], 1))