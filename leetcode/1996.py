from typing import *
from functools import cmp_to_key


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans: int = 0
        maxDef: int = 0
        for att, defence in properties:
            if maxDef > defence:
                ans += 1
            else:
                maxDef = max(maxDef, defence)
        return ans


a = Solution()
print(a.numberOfWeakCharacters([[2, 2], [3, 3]]))
