from typing import List

class Solution:
    def minCut(self, s: str) -> int:
        def ishuiWen(txt:str):
            return txt == txt[::-1]
        
        len_s = len(s)
        dp = [len_s+1]*len_s
        for i in range(len_s):
            if ishuiWen(s[0:i+1]):
                dp[i] = 0
            else:
                for j in range(0,i):
                    if ishuiWen(s[j+1:i+1]):
                        dp[i] = min(dp[j]+1,dp[i])
        return dp[len_s-1]
        pass

a =Solution()
print(a.minCut("ab"))