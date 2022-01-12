# https://leetcode-cn.com/problems/increasing-triplet-subsequence/
from typing import *


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        leftmin = [nums[0]]
        for i in range(1, len(nums)):
            leftmin.append(min(leftmin[i-1], nums[i]))
        rightmax = [0]*len(nums)
        rightmax[len(nums)-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], nums[i])
        for i in range(1, len(nums)-1):
            if leftmin[i-1] < nums[i] < rightmax[i+1]:
                return True
        return False


class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        fir, sec = nums[0], (1 << 32)
        for i in range(1, len(nums)):
            t = nums[i]
            if t > sec:
                return True
            elif t > fir:
                sec = t
            else:
                fir = t
        return False


a = Solution1()
print(a.increasingTriplet([5, 4, 3, 2, 1]))
