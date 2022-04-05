from typing import *


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def check(x: int) -> bool:
            nums1 = 0
            while x > 0:
                nums1 += x % 2
                x //= 2
            if nums1 == 1:
                return False
            for i in range(2, nums1):
                if i*i > nums1:
                    break
                if nums1 % i == 0:
                    return False
            return True
        ans = 0
        for i in range(left, right+1):
            if check(i):
                ans += 1
        return ans


a = Solution()
print(a.countPrimeSetBits(10, 15))
