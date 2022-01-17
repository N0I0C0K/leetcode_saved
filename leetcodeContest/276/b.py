class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        t = 0
        res = 0
        while target > 1:
            if target % 2 == 1:
                target -= 1
                res += 1
            else:
                if t < maxDoubles:
                    target = target//2
                    res += 1
                    t += 1
                else:
                    res += target-1
                    break
        return res


a = Solution()
print(a.minMoves(10, 4))
