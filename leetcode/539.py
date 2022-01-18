# https://leetcode-cn.com/problems/minimum-time-difference/

from typing import *
from functools import cmp_to_key


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def cmp(a: str, b: str) -> bool:
            if a[0:2] != b[0:2]:
                return int(a[0:2])-int(b[0:2])
            else:
                return int(a[3:])-int(b[3:])

        def ctime(a: str, b: str) -> int:
            tmp = (int(a[0:2])*60+int(a[3:]))-(int(b[0:2])*60+int(b[3:]))
            tmp = min(1440-tmp, tmp)
            return tmp
        timePoints.sort(key=cmp_to_key(cmp), reverse=True)
        res = 10000
        for i in range(0, len(timePoints)-1):
            res = min(res, ctime(timePoints[i], timePoints[i+1]))
        res = min(res, ctime(timePoints[0], timePoints[-1]))
        return res


a = Solution()
print(a.findMinDifference(["00:00", "04:00", "22:00"]))
