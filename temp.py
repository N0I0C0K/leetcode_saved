class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        a = 0
        if s[0] == '-':
            s = s[1:]
            s = s[::-1]
            a =  int(s)*-1
        else:
            s = s[::-1]
            a = int(s)
        if a > 2147483647 or a < -2147483648:
            return 0
        return a
a = Solution()
print(a.reverse(-1))