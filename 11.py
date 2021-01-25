from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        left = 0
        right = len(height)-1
        while left<right:
            squ = (right-left)*min(height[left], height[right])
            max_ = max(max_, squ)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_