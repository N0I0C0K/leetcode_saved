from typing import *


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = nums[0]
        ans = -1
        for i in range(1, len(nums)):
            t = nums[i]
            if t > m:
                ans = max(t-m, ans)
            m = min(m, t)
        return ans


a = Solution()
print(a.maximumDifference([9, 4, 4, 2]))
