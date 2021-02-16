# 474. 一和零   https://leetcode-cn.com/problems/ones-and-zeroes/
# 
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        nums = 0
        m_n = m+n
        for item in strs:
            if len(item) > m_n:
                continue
            m_all = 0
            n_all = 0
            for i in range(len(item)):
                if item[i] == '1':
                    n_all += 1
                else:
                    m_all += 1
            if m_all <= m and n_all <= n:
                nums+=1

        return nums
