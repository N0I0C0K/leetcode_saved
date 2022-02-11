from typing import *


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1000010
        for i in range(k-1, len(nums)):
            ans = min(ans, nums[i]-nums[i-k+1])
        return ans


a = Solution()
print(a.minimumDifference([9, 4, 1, 7], 2))
