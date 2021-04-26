from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp,g = [0]*n, [0]*n
        max_len = 0
        max_idx = 0
        for i in range(n):
            length, pre = 1,i
            for j in range(i):
                if nums[i]%nums[j] == 0 and dp[j]+1>length:
                    length = dp[j]+1
                    pre = j
            dp[i] = length
            g[i] = pre
            if length > max_len:
                max_len = length
                max_idx = i
        
        ans = []
        while len(ans) < max_len:
            ans.append(nums[max_idx])
            max_idx = g[max_idx]
        ans.reverse()
        return ans


a = Solution()
print(a.largestDivisibleSubset([1,2,6,4,8,3]))