from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_f = len(flowerbed)
        nums = 0
        if n == 0 and len_f > 0:
            return True
        if len_f == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False

        for i in range(len_f):
            if i>0 and i<len_f-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    nums+=1
                    flowerbed[i] += 1
            elif i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] += 1
                    nums+=1
            elif i == len_f-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] += 1
                    nums+=1
        return nums>=n

a = Solution()
a.canPlaceFlowers([1,0,0,0,1],1)