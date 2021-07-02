from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = len(nums)
        nums.sort()
        n = 1
        for i in range(1,a):
            if n > a/2:
                return nums[i-1]
            if nums[i] != nums[i-1]:
                n = 1
            else:
                n+=1
        if n > a/2:
            return nums[-1]

a = Solution()
print(a.majorityElement([2,2,1,1,1,2,2]))