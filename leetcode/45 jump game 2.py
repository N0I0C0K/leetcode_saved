from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        rod = [1000]*len(nums)
        rod[0] = 0
        len_n = len(nums)
        for i in range(len(nums)):
            if i == len(nums)-1:
                return rod[i]
            for j in range(i+1, min(i+1+nums[i], len_n)):
                rod[j] = min(rod[j], rod[i]+1)


a = Solution()
print(a.jump([2,1]))

