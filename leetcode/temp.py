from typing import *


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        i = 0
        while i < l:
            if i + 1 == l:
                return True
            a = bits[i]
            if a == 1:
                i += 1
            i += 1
        return False
