from typing import *
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = right = cnt = 0
        queMax = deque()
        queMin = deque()
        while right < (l := len(nums)):
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()
            queMin.append(nums[right])
            queMax.append(nums[right])
            while queMax and queMin and queMax[0]-queMin[0] > limit:
                if nums[left] == queMin[0]:
                    queMin.popleft()
                if nums[left] == queMax[0]:
                    queMax.popleft()
                left += 1
            cnt = max(cnt, right-left+1)
            right += 1
        return cnt


a = Solution()
print(a.longestSubarray([8, 2, 4, 7], 4))
