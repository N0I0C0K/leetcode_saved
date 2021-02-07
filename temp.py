#简单题的容身之处

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        len_n = len(nums)
        if len_n == 1:
            return True
        m_num = 0
        for i in range(len_n):
            if i == 0:
                if nums[i] > nums[i+1]:
                    m_num += 1
                    continue
            elif i == len_n - 1:
                if nums[i] < nums[i-1]:
                    m_num += 1
                    continue
            else:
                if nums[i] < nums[i-1] or nums[i] > nums[i+1]:
                    m_num += 1
                    continue
            if m_num >= 2:
                return False
        return True
