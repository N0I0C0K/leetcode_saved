from typing import List
#第一种思路，其实就是二分查找加插入，但是时间不是最快的

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
    def bsearch(self, val: int)->int:
        left, right = 0, len(self.nums)
        while left < right:
            mid = int((left+right)/2)
            if val > self.nums[mid]:
                left = mid+1
            elif val < self.nums[mid]:
                right = mid
            else:
                return mid
        return left

    def add(self, val: int) -> int:
        self.nums.insert(self.bsearch(val), val)
        return self.nums[len(self.nums)-self.k]

a = KthLargest(3, [4, 5, 8, 2])
while True:
    i = int(input())
    print(a.add(i))