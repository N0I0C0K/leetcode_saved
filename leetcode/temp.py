from typing import *


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = 1e5
        for i, t in enumerate(nums):
            if t == target:
                res = min(abs(i-start), res)
        return res
