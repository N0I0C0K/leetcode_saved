class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = (1, 1, 1, 1, 1)  # a,e,i,o,u
        m = 1000000007
        for _ in range(n-1):
            dp = ((dp[1]+dp[2]+dp[4]) % m, (dp[0]+dp[2]) %
                  m, (dp[1]+dp[3]) % m, dp[2] % m, (dp[2]+dp[3]) % m)
        return sum(dp) % m
