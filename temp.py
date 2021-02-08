#简单题的容身之处

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        len_n = len(nums)
        if len_n == 1:
            return True
        m_num = 0
        num_t = None
        for i in range(len_n):
            if i < len_n - 1:
                if num_t is not None:
                    if nums[i] < num_t:
                        m_num += 1
                    else:
                        num_t = None
                elif nums[i] > nums[i+1]:
                    num_t = nums[i]
                    m_num += 1
            if m_num >= 2:
                return False
        return True
