from typing import *
from functools import cmp_to_key
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def cmp(ls, rs):
            if ls < 0 and rs < 0:
                return rs-ls
            return ls - rs
        arr.sort(key=cmp_to_key(cmp))
        l = len(arr)
        data = Counter()
        for i in range(0, l):
            t = arr[i]
            if not (t & 1) and data[t//2] > 0:
                data[t//2] -= 1
            else:
                data[t] += 1
        return max(data.values()) == 0


a = Solution()
print(a.canReorderDoubled([8, 8, 2, 4]))
