from typing import *


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        l = len(arr)
        dp = [1]*l
        data: Dict[int, int] = dict()
        for i in range(l):
            if arr[i]-difference in data:
                dp[i] = max(dp[i], dp[data[arr[i]-difference]]+1)
            data[arr[i]] = i
        return max(dp)


a = Solution()
print(a.longestSubsequence([1, 3, 5, 7], 1))
