#https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/
#动态规划 滑动窗口

#补充几句，思路转化真的很重要，这道题乍一看像是动态规划其实不然，转化一下思路才是关键

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_ = 0
        all_ = 0
        len_c = len(cardPoints)
        for i in range(len_c):
            max_ = max_ + cardPoints[i] if i < len_c-k else max_
            all_ += cardPoints[i]
        all = max_
        start, end = 0, len_c - k
        while end < len_c:
            all = all - cardPoints[start] + cardPoints[end]
            start+=1
            end+=1
            if all < max_:
                max_ = all
        return all_-max_

a = Solution()
print(a.maxScore([1,2,3,4,5,6,1],3))