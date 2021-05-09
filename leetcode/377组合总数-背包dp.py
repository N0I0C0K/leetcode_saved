from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]+[0]*target
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

a = Solution()
print(a.combinationSum4([1,2,3],4))