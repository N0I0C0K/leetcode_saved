from typing import List
import heapq

'''
heapq 默认最小堆,通过插入变负数改变单调性来变成最大堆.

'''


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        len_n = len(nums)
        dp = [-1e9]*(len_n)
        heap = []
        dp[0] = nums[0]
        heapq.heappush(heap, (-dp[0], 0))
        for i in range(1,len_n):
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            dp[i] = -heap[0][0]+nums[i]
            #heapq.heappop(heap)
            heapq.heappush(heap, (-dp[i], i))
        return dp[len_n-1]

class Solution1:
    def maxResult(self, nums: List[int], k: int) -> int:
        

a = Solution()
print(a.maxResult([1,-5,-20,4,-1,3,-6,-3],2))