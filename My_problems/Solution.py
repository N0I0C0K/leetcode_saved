from typing import List
import heapq
import random

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
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

def generateData(n:int,k:int, idx:str):
    nums = [random.randint(-100, 500) for _ in range(n)]
    so = Solution()
    res = so.maxResult(nums, k)
    
    with open(f'input-{idx}.txt','w') as file:
        file.write(f'{n} {k}\n')
        file.write(str(nums).replace(',', ' ')[1:-1]+'\n')
        pass
    with open(f'out-put{idx}.txt', 'w') as file:
        file.write(f'{res}')

if __name__ == '__main__':
    generateData(5000, 1000,5)
