from typing import *


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            can = False
            for i, (n, ch) in enumerate(cnt):
                if n <= 0:
                    break
                if len(ans) >= 2 and ch == ans[-1] and ch == ans[-2]:
                    continue
                can = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not can:
                return ''.join(ans)


a = Solution()
print(a.longestDiverseString(1, 1, 7))
