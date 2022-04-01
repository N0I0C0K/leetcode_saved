from typing import *


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        def check(n: int) -> bool:
            n_s = str(n)
            for i in n_s:
                if i == '0' or n % int(i) != 0:
                    return False
            return True

        for i in range(left, right+1):
            if check(i):
                res.append(i)
        return res


a = Solution()
print(a.selfDividingNumbers(1, 22))
