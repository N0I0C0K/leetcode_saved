class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        k = n//7
        res += k*28
        if k > 0:
            res += 7*(0+(k-1))*k//2
        for i in range(n % 7):
            res += i+1+k
        return res


a = Solution()
print(a.totalMoney(20))
