'''
dp[i][j] 表示[i,j]是否为回文字符串
dp[i-1][j+1] = dp[i][j] and s[i-1]==s[j+1]
dp[i][i+1] = s[i] == s[i+1]
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(2, n+1):
            for j in range(0,n):
                r = j+i-1
                if r>=n:
                    break
                if s[j] != s[r]:
                    dp[j][r] = False
                    continue
                else:
                    if i == 2:
                        dp[j][r] = True
                    else:
                        dp[j][r] = dp[j+1][j+i-2]
                    if dp[j][r] and i > max_len:
                        max_len = i
                        begin = j
        return s[begin:begin+max_len]
    
a = Solution()
print(a.longestPalindrome('a'))