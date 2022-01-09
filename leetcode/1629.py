from typing import *
from functools import cmp_to_key


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        temp = []
        temp.append((releaseTimes[0], keysPressed[0]))
        for i in range(1, len(releaseTimes)):
            temp.append((releaseTimes[i]-releaseTimes[i-1], keysPressed[i]))

        def cmp(li, ri):
            if li[0] < ri[0]:
                return -1
            elif li[0] > ri[0]:
                return 1
            else:
                return ord(li[1])-ord(ri[1])
        temp.sort(key=cmp_to_key(cmp), reverse=True)
        return temp[0][1]


a = Solution()
print(a.slowestKey([9, 29, 49, 50], "cbcd"))
