from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        num = 0
        index = 0
        for i in s:
            for j in range(index, len(g)):
                if i >= g[j]:
                    num += 1
                    index += 1
                    break
        return num