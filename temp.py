#简单题的容身之处--划水哈哈哈哈哈哈

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        len_n = len(nums)
        temp_num = 0
        for i in range(len_n):
            if nums[i] == 1:
                temp_num += 1
            else:
                temp_num = 0
            if temp_num > max_num:
                max_num = temp_num
        return max_num
