from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0 for i in range(self.n+1)]
        for i, val in enumerate(nums):
            self.__update(i, val)
        self.ynums = nums.copy()

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def __update(self, index: int, val: int) -> None:
        i = index+1
        while i <= self.n:
            self.nums[i] += val
            i += self.lowbit(i)

    def update(self, index: int, val: int) -> None:
        k = val - self.ynums[index]
        self.ynums[index] = val
        self.__update(index, k)

    def getSum(self, idx: int) -> int:
        ans = 0
        i = idx
        while i > 0:
            ans += self.nums[i]
            i -= self.lowbit(i)
        return ans

    def sumRange(self, left: int, right: int) -> int:
        left += 1
        right += 1
        return self.getSum(right)-self.getSum(left-1) if left > 1 else self.getSum(right)


def test():
    a = NumArray([1, 3, 5])
    a.update(1, 2)
    print(a.sumRange(0, 2))


test()
