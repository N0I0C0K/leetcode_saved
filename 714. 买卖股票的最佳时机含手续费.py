from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        buy = prices[0]+fee
        for i in range(1, len(prices)):
            if prices[i]+fee < buy:
                buy = prices[i]+fee
            elif prices[i] > buy:
                res += prices[i]-buy
                buy = prices[i]
        return res

a = Solution()
print(a.maxProfit([2,1,4,4,2,3,2,5,1,2],1))