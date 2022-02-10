from typing import *


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        def divide(k: int) -> list:
            div = []
            for i in range(2, k):
                if i*i > k:
                    break
                if k % i == 0:
                    div.append(i)
                    while k % i == 0:
                        k = k//i
            if k > 1:
                div.append(k)
            return div
        ans: List[str] = []
        for i in range(2, n+1):
            div = divide(i)
            for j in range(1, i):
                for d in div:
                    if j % d == 0:
                        break
                else:
                    ans.append(f'{j}/{i}')
        return ans


a = Solution()
print(a.simplifiedFractions(6))
