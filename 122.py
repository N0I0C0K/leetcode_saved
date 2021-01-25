from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        #temp = []
        for i in range(0, len(prices)-1):
            temp = prices[i+1]-prices[i]
            if temp > 0:
                res+=temp
        return res