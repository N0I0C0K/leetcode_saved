from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        max_index = 0
        for i, value in enumerate(nums):
            if max_index == len_nums-1:
                return True
            if max_index == i and value == 0:
                return False
            if i+value > max_index:
                max_index = i+value
        return True


so = Solution()
print(so.canJump([0]))