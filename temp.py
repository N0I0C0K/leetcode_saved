from typing import List

class NumArray:
    sum:list = None
    def __init__(self, nums: List[int]):
        temp = 0
        self.sum = []
        for num in nums:
            self.sum.append(temp)
            temp+=num
        self.sum.append(temp)
        pass

    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right+1]-self.sum[left]
        pass