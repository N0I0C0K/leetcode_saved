from typing import *


class UUnion:
    far: List[int] = None
    cnt: int = 0

    def __init__(self, n: int) -> None:
        self.far = [i for i in range(n)]
        self.cnt = n
        pass

    def find(self, x: int) -> int:
        if x == self.far[x]:
            return x
        nf = self.find(self.far[x])
        self.far[x] = nf
        return nf

    def merge(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.cnt -= 1
        self.far[rx] = ry


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = int(len(row)/2)
        union = UUnion(n)
        for i in range(0, len(row), 2):
            union.merge(row[i] >> 1, row[i+1] >> 1)
        return n-union.cnt
