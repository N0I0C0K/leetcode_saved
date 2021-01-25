from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = -1
        max_ = -1
        max_res = 0
        len_price = len(prices)
        if len_price == 0:
            return max_res
        for i in range(len_price):
            tar = prices[i]
            if min_ == -1 or tar < min_:
                min_ = tar
                max_ = tar
            elif tar > max_:
                max_ = tar
                max_res = max(max_res, max_-min_)
        return max_res

a = Solution()
print(a.maxProfit([7,6,4,3,1]))