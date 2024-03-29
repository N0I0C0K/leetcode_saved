# 300. 最长递增子序列
# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# 简单的动态规划

from typing import List

class Solution_2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_n = len(nums)
        dp = [0]*(len_n+1)
        dp[1] = nums[0]
        index = 1
        def BinarySearch(i:int, a:int) -> int:
            left, right = 1, i 
            while left < right:
                mid = int((left+right)/2)
                if dp[mid] >= a:
                    right = mid
                else:
                    left = mid + 1
            return right
        for i in range(1,len_n):
            if nums[i] > dp[index]:
                index += 1
                dp[index] = nums[i]
            else:
                dp[BinarySearch(index, nums[i])] = nums[i]
        return index

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l_n = len(nums)
        dp = [1]*l_n
        for i in range(1,l_n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

        
a =Solution()
print(a.lengthOfLIS([1,3,6,7,9,4,10,5,6]
))