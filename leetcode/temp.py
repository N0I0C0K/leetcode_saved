from typing import *


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mmap: Dict[str, int] = {}
        for item in (s1+' '+s2).split():
            if item in mmap:
                mmap[item] += 1
            else:
                mmap[item] = 1
        res = []
        for key, val in mmap.items():
            if val == 1:
                res.append(key)
        return res


a = Solution()
print(a.uncommonFromSentences('this apple is sweet sweet', 'this apple is sour'))
