from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        all = 0
        for i in nums:
            all+=i
        if all<=goal:
            all = goal - all
            if all % limit == 0:
                return int(all/limit)
            else:
                return int(all/limit)+1
        else:
            all = all-goal
            if all % limit == 0:
                return int(all/limit)
            else:
                return int(all/limit)+1

