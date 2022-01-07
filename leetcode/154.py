# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) >> 1
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return min(nums[left], nums[right])


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        ti = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                ti = i+1
                break
        return min(nums[0], nums[ti])


a = Solution()
print(a.findMin([3, 3, 1, 3]))
