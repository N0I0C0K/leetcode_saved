#简单题的容身之处

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        MAX = len(nums)
        num = [0]*(MAX+1)
        for i in nums:
            num[i] = i
        re = []
        for i in range(1,MAX+1):
            if num[i] != i:
                re.append(i)
        return re


