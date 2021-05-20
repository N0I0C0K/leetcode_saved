from typing import List

class Solution_pre:
    def canPartition(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        tar:int = 0
        for i in nums:
            tar+=i
        if tar%2 != 0:
            return False
        tar = int(tar/2)
        dp = [[False]*( tar+1) for i in range(len_nums)]
        if nums[0] <= tar:
            dp[0][nums[0]] = True
        for i in range(1, len_nums):
            for j in range(tar+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]

        return dp[len_nums-1][tar]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)
        if n%2 != 0:
            return False
        m = int(n/2)
        dp = [False]*(m+1)
        dp[0] = True
        for num in nums:
            for i in range(m,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
        return dp[m]

a = Solution()
print(a.canPartition([1, 5, 11, 5,4]))