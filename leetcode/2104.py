from typing import *
from collections import deque


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans: int = 0
        for i in range(2, len(nums)+1):
            mind: Deque[int] = deque()
            maxd: Deque[int] = deque()
            for j, num in enumerate(nums):
                while len(mind) and nums[mind[-1]] < num:
                    mind.pop()
                mind.append(j)
                if j >= i-1:
                    while len(mind) and mind[0] < j-i+1:
                        mind.popleft()
                while len(maxd) and nums[maxd[-1]] > num:
                    maxd.pop()
                maxd.append(j)
                if j >= i-1:
                    while len(maxd) and maxd[0] < j-i+1:
                        maxd.popleft()
                    ans += nums[mind[0]]-nums[maxd[0]]
        return ans


a = Solution()
print(a.subArrayRanges([1, 3, 3]))
