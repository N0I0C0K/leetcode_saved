# https://leetcode-cn.com/problems/divide-two-integers/
# 两数相除, 要求不使用除法

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor < 0):
            res = 0-self.divide(dividend, 0-divisor)
            return res if res < 2147483648 and res >= -2147483648 else 2147483647
        elif dividend < 0 and divisor > 0:
            res = 0-self.divide(0-dividend, divisor)
            return res if res < 2147483648 and res >= -2147483648 else 2147483647
        elif dividend < 0 and divisor < 0:
            res = self.divide(0-dividend, 0-divisor)
            return res if res < 2147483648 and res >= -2147483648 else 2147483647
        if dividend >= divisor:
            res = 1
            tb = divisor
            while tb+tb <= dividend:
                res += res
                tb += tb
            res = res + self.divide(dividend-tb, divisor)
            return res
        else:
            return 0


a = Solution()
print(a.divide(-2147483648, -1))
