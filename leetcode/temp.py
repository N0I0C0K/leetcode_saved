from typing import *


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums = list(enumerate(nums))
        nums.sort(reverse=True, key=lambda x: x[1])
        if nums[0][1] >= nums[1][1]*2:
            return nums[0][0]
        else:
            return -1


a = Solution()
print(a.dominantIndex([3, 6, 1, 0]))
