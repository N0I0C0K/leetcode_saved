from typing import *


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix0 = [0]
        prefix1 = [0]
        cnt0, cnt1 = 0, 0
        mmax = 0
        ans: Dict[int, List[int]] = {}
        for i in nums:
            if i == 0:
                cnt0 += 1
            else:
                cnt1 += 1
            prefix1.append(cnt1)
            prefix0.append(cnt0)
        for i in range((n := len(nums))+1):
            t = prefix0[i]+prefix1[n]-prefix1[i]
            mmax = max(t, mmax)
            if t in ans:
                ans[t].append(i)
            else:
                ans[t] = [i]
        return ans[mmax]


a = Solution()
print(a.maxScoreIndices([1, 1]))
