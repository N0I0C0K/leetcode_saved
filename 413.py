from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0]*len(nums)
        if nums[2]+nums[0] == 2*nums[1]:
            dp[2] = 1
        for i in range(3,len(nums)):
            if nums[i]+nums[i-2] == 2*nums[i-1]:
                dp[i] = dp[i-1]+1
        total = sum(dp)
        return total


a = Solution()
print(a.numberOfArithmeticSlices([1,2,3,4]))