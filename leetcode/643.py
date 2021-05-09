# 643. 子数组最大平均数 I
# https://leetcode-cn.com/problems/maximum-average-subarray-i/
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        len_n = len(nums)
        max_num = 0
        for j in range(0,k):
            max_num += nums[j]
        temp = nums[0]
        all_pre = max_num
        for i in range(1, len_n-k+1):
            all = all_pre
            all += (nums[i+k-1]-temp)
            temp = nums[i]
            all_pre = all
            if all > max_num:
                max_num = all
        return max_num/k