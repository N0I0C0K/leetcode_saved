# https://leetcode-cn.com/problems/contains-duplicate-ii/

from typing import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mnums = dict()
        for i in range(len(nums)):
            if nums[i] in mnums and abs(i - mnums[nums[i]]) <= k:
                return True
            else:
                mnums[nums[i]] = i
        return False


a = Solution()
print(a.containsNearbyDuplicate([1, 2, 3, 1], 3))
