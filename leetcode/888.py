from typing import List

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a_d = dict()
        b_d = dict()
        a_a = 0
        b_a = 0
        for i in A:
            a_a += i
            a_d[i] = 1
        for i in B:
            b_a += i
            b_d[i] = 1
        k = int((b_a-a_a)/2)
        for i in a_d.keys():
            if i+k in b_d:
                return [i,i+k]


a = Solution()
print(a.fairCandySwap([1,2,5],[2,4]))