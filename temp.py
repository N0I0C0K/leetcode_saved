#简单题的容身之处--划水哈哈哈哈哈哈

from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        h = len(nums)
        w = len(nums[0])
        if h*w != r*c:
            return nums
        re = []
        n = 0
        temp = []
        for item in nums:
            for i in item:
                if n < c:
                    temp.append(i)
                    n += 1
                if n == c:
                    re.append(temp)
                    temp = []
                    n = 0
        return re