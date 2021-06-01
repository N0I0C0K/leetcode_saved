'''
位运算判断是否为2的幂

只需要判断除了最高位其他地方是否有1就行了=>n&(n-1) = 0    ---->比如 1000 & (0111) = 0

通过n&(n-1) == 0判断

'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n&(n-1) == 0