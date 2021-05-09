from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_n = max(nums)
        total = [0]*(max_n+1)
        for num in nums:
            total[num] += num
        pre, cur = total[0], max(total[0], total[1])
        for i in range(2, max_n+1):
            pre, cur = cur, max(pre+total[i], cur) 
        return cur