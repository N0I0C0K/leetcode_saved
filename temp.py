#简单题的容身之处--划水哈哈哈哈哈哈
#2-24
#忙了几天，终于有时间
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start, end = 0, -1
        max_len = 0
        while start < len(nums):
            max_t = nums[start]
            min_t = nums[start]
            for i in range(start, len(nums)):
                end += 1
                if nums[end] > max_t:
                    max_t = nums[end]
                elif nums[end] < min_t:
                    min_t = nums[end] 
                if abs(max_t - min_t) <= limit:
                    continue
                else:
                    if end - start > max_len:
                        max_len = end -start
                    break
            else:
                if end - start + 1 > max_len:
                    max_len = end -start + 1
            end = start
            start += 1
        return max_len

a = Solution()
print(a.longestSubarray([10,1,2,4,7,2], 5))