from typing import *


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        i = 1
        num1 = num+1
        num2 = num+2
        a, b = 1, num2
        while i*i <= num2:
            if num1 % i == 0 and abs(num1//i - i) < abs(a-b):
                a, b = i, num1//i
            if num2 % i == 0 and abs(num2//i - i) < abs(a-b):
                a, b = i, num2//i
            i += 1
        return [a, b]


so = Solution()
print(so.closestDivisors(1))
