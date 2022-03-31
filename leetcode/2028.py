from typing import *


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        asum = mean*(n+len(rolls))-sum(rolls)
        if asum > 6*n or asum < n:
            return []
        res = [1]*n
        asum -= n
        for i in range(n):
            if asum <= 0:
                break
            res[i] += min(5, asum)
            asum -= 5
        return res
