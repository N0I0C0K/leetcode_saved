class Solution:
    def numSquares(self, n: int) -> int:
        def isSq(nu:int)->bool:
            for i in range(1,nu):
                if i*i == nu:
                    return True
                if i*i > nu:
                    return False
        dp = [0]*(n+1)
        dp[1] = 1
        nums = [1]
        for i in range(2,n+1):
            if isSq(i):
                dp[i] = 1
                nums.append(i)
            else:
                dp[i] = i
                for num in nums:
                    dp[i] = min(dp[i], dp[i-num]+1)
        return dp[n]

a = Solution()
print(a.numSquares(55))

