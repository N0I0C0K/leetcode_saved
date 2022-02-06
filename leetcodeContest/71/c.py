from typing import *


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        tar: List[str] = []
        if targetSeconds < 100:
            tar.append(str(targetSeconds))
        if targetSeconds < 6000:
            if targetSeconds % 60 < 10:
                tar.append(f'{targetSeconds//60}0{targetSeconds%60}')
            else:
                tar.append(f'{targetSeconds//60}{targetSeconds%60}')
        if targetSeconds % 60 < 40 and targetSeconds//60 >= 1:
            if targetSeconds//60 >= 2:
                tar.append(f'{(targetSeconds//60) -1}{(targetSeconds%60)+60}')
            else:
                tar.append(f'{(targetSeconds%60)+60}')

        def cost(s: str) -> int:
            c: int = 0
            if int(s[0]) != startAt:
                c += moveCost
            c += len(s)*pushCost
            for i in range(1, len(s)):
                if s[i] != s[i-1]:
                    c += moveCost
            return c
        return min(cost(co) for co in tar)


a = Solution()
print(a.minCostSetTime(3, 1, 9, 6000))
