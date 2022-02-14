from typing import *


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = {key: 0 for key in 'balloon'}
        for i in text:
            if i in ans:
                if i in 'lo':
                    ans[i] += 1
                else:
                    ans[i] += 2
        r = min(ans.values())
        return r >> 1 if (r & 1 == 0) else (r-1) >> 1


a = Solution()
print(a.maxNumberOfBalloons('ballon'))
