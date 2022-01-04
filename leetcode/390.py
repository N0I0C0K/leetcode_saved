class Solution:
    def lastRemaining(self, n: int) -> int:
        k = 0
        a, step, count = 1, 1, n
        while count > 1:
            if k % 2 == 0:
                a += step
            else:
                if count % 2 == 1:
                    a += step
            step <<= 1
            count >>= 1
            k += 1
        return a


a = Solution()
print(a.lastRemaining(29))
