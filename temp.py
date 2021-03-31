from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            temp = []
            for j in range(i, len(nums)):
                temp.append(nums[j])
                res.append(temp.copy())
        return res

a = Solution()
print(a.subsetsWithDup([1,2,2]))