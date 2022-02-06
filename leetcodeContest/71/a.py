class Solution:
    def minimumSum(self, num: int) -> int:
        w = list(map(int, str(num)))
        w.sort()
        return (w[0]+w[1])*10+(w[2]+w[3])


a = Solution()
print(a.minimumSum(4009))
