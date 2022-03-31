from typing import *


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre, now = n % 2, 0
        n //= 2
        while n > 0:
            now = n % 2
            if now == pre:
                return False
            pre = now
            n //= 2
        return True


a = Solution()
print(a.hasAlternatingBits(11))
