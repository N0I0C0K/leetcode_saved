class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = []
        isd = False
        if num < 0:
            isd = True
            num *= -1
        while num > 0:
            res.append(str(num % 7))
            num //= 7
        t = ''
        for i in range(len(res)-1, -1, -1):
            t = t+res[i]
        if isd:
            t = '-'+t
        return t


a = Solution()
print(a.convertToBase7(-11))
