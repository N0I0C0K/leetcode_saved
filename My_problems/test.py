import heapq

class Solution:
    def maxResult(self, nums:list, k: int) -> int:
        len_n = len(nums)
        dp = [-1e9]*(len_n)
        heap = []
        dp[0] = nums[0]
        heapq.heappush(heap, (dp[0], 0))
        for i in range(1,len_n):
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            dp[i] = heap[0][0]+nums[i]
            #heapq.heappop(heap)
            heapq.heappush(heap, (dp[i], i))
        return dp[len_n-1]

n,k = map(int, input().split())
nums = list(map(int, input().split()))
a = Solution()
print(a.maxResult(nums, k))