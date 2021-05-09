import altgraph

class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        b = ''
        if(a[0] == '-'):
            b = a[1::-1]
            b = '-'+b
        else:
            b = a[::-1]
        print(b)


a = Solution()
a.reverse(-321)