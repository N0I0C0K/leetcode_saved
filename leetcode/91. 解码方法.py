class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        dp[0] = 1 if int(s[0]) > 0 else 0
        for i in range(1,len(s)):
            if int(s[i]) > 0:
                dp[i] += dp[i-1]
            if s[i-1] != '0' and int(s[i-1]+s[i]) > 0 and int(s[i-1]+s[i]) < 27:
                if i>1: 
                    dp[i] += dp[i-2]
                elif i == 1:
                    dp[i] += 1
        return dp[len(s)-1]

a = Solution()
print(a.numDecodings('27'))