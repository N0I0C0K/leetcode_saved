from typing import *


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter()
        for a in nums:
            ans += cnt[a-k]+cnt[a+k]
            cnt[a] += 1
        return ans


a = Solution()
print(a.countKDifference([1, 3], 2))
