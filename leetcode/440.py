class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getStep(cur: int) -> int:
            steps, fir, last = 0, cur, cur
            while fir <= n:
                steps += min(last, n)-fir+1
                fir *= 10
                last = last*10+9
            return steps

        cur = 1
        k -= 1
        while k:
            step = getStep(cur)
            if step <= k:
                k -= step
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur
