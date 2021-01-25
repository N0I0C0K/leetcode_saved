from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        all = 1
        inc, dec, pre = 1, 0, 1
        for i in range(1,n):
            if ratings[i] >= ratings[i-1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i-1] else pre+1)
                all += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                all += dec
                pre = 1
        return all

a = Solution()
print(a.candy([3,3,4,5,3,2,1,2,1,0,4,3]))