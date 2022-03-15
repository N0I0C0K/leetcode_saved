from typing import *


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxn = 0
        n = len(nums)
        res = 0
        for num in nums:
            maxn |= num

        def dfs(idx: int, t: int = 0):
            nonlocal res, maxn, n
            if idx == n:
                if t == maxn:
                    res += 1
                return
            dfs(idx+1, t)
            dfs(idx+1, t | nums[idx])
        dfs(0)
        return res


a = Solution()
print(a.countMaxOrSubsets([3, 2, 1, 5]))
