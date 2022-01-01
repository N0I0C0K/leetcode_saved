from typing import *
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        resAll: int = 1
        for i in range(2, num):
            if i*i > num:
                break
            if num % i == 0:
                resAll = resAll+i+num//i
        return resAll == num and num != 1


so = Solution()
print(so.checkPerfectNumber(2))
