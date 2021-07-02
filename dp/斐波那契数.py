class Solution:
    def fib(self, n: int) -> int:
        dp = [0]*40
        dp[1] = 1
        dp[2] = 1
        if n <= 2:
            return dp[n]
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]

a = Solution()
print(a.fib(3))