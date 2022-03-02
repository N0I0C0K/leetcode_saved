from math import *


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k = 2*numRows-2
        if k == 0:
            return s
        l = len(s)
        nums = ceil(l/k)
        res = []
        for i in range(numRows):
            for j in range(nums):
                if i+j*k < l:
                    res.append(s[i+j*k])
                if 0 < i < numRows-1 and j*k+k-i < l:
                    res.append(s[j*k+k-i])
        return ''.join(res)


a = Solution()
print(a.convert('PAYPALISHIRING', 4))
