# https://leetcode-cn.com/problems/gray-code/
from typing import *


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            lres = len(res)
            for j in range(lres-1, -1, -1):
                res.append(res[j]+(1 << (i-1)))
        return res


so = Solution()
print(so.grayCode(5))
