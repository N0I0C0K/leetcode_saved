from typing import *


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x1, y1 = int(num1[:num1.index('+')]), int(num1[num1.index('+')+1:-1])
        x2, y2 = int(num2[:num2.index('+')]), int(num2[num2.index('+')+1:-1])
        x = x1*x2-y1*y2
        y = x1*y2+y1*x2
        return f'{x}+{y}i'


a = Solution()
print(a.complexNumberMultiply('1+-1i', '1+-1i'))
