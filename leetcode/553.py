from typing import *


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        l = len(nums)
        if l == 1:
            return str(nums[0])
        elif l == 2:
            return '/'.join(map(str, nums))
        else:
            return str(nums[0])+'/('+'/'.join(map(str, nums[1:]))+')'
