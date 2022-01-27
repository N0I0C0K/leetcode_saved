from typing import *
from collections import defaultdict


class DetectSquares:
    _mmap: DefaultDict[int, List[int]] = None

    def __init__(self):
        self._mmap = defaultdict(Counter)
        pass

    def add(self, point: List[int]) -> None:
        x, y = point
        self._mmap[y][x] += 1
        pass

    def count(self, point: List[int]) -> int:
        ans: int = 0
        x, y = point
        if not y in self._mmap:
            return 0
        yCnt = self._mmap[y]
        for col, colCnt in self._mmap.items():
            if col != y:
                d = col-y
                ans += colCnt[x]*yCnt[x+d]*colCnt[x+d]
                ans += colCnt[x]*yCnt[x-d]*colCnt[x-d]
        return ans


sol = DetectSquares()
sol.add([3, 10])
sol.add([11, 2])
sol.add([3, 2])
print(sol.count([11, 10]))
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
