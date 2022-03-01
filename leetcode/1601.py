from typing import *


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        detal: List[int] = [0]*n
        ans, cnt, zero = 0, 0, n
        l = len(requests)

        def dfs(pos: int):
            nonlocal ans, cnt, zero, detal
            if pos == l:
                if zero == n:
                    ans = max(cnt, ans)
                return
            dfs(pos+1)
            x, y = requests[pos]
            z = zero
            cnt += 1
            zero -= detal[x] == 0
            detal[x] -= 1
            zero += detal[x] == 0
            zero -= detal[y] == 0
            detal[y] += 1
            zero += detal[y] == 0
            dfs(pos+1)
            detal[x] += 1
            detal[y] -= 1
            cnt -= 1
            zero = z

        dfs(0)
        return ans


a = Solution()
print(a.maximumRequests(3, [[0, 0], [1, 2], [2, 1]]))
