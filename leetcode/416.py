from typing import List

class Solution:
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


a = Solution()
print(a.canPartition([1, 5, 11, 5,4]))