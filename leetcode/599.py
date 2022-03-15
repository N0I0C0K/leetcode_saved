from typing import *


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        data = {}
        for i, t in enumerate(list1):
            data[t] = i
        mn = 2000
        ans = []
        for i, t in enumerate(list2):
            if t in data:
                if data[t]+i < mn:
                    mn = data[t]+i
                    ans = [t]
                elif data[t]+i == mn:
                    ans.append(t)
        return ans
