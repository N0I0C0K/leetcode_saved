class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i]+=1
            t:str = s[i-1]+s[i]
            n = int(t)
            if s[i-1] != '0':
                if n > 0 and n < 27:
                    dp[i]+=1
            else:
                if int(s[i-2:i])<27 and int(s[i-2:i]) > 0:
                    dp[i]+=1
                if s[i] != '0':
                    dp[i]+=1
        return dp[len(s)-1]

a = Solution()
print(a.numDecodings('06'))