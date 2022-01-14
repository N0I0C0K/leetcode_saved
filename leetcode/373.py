from typing import *


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        s1, e1 = 0, 0
        s2, e2 = 0, 0
        res = []
        while len(res) < k:
            if nums1[s1]+nums2[e2] < nums1[s2]+nums1[e1]:
                res.append([nums1[s1], nums2[e2]])
                e2 += 1
                if e2 == len(nums2):
                    s1 += 1
                    e2 = s2+1
            else:
                res.append([nums2[s2], nums1[e1]])
                e1 += 1
                if e1 == len(nums1):
                    s2 += 1
                    e1 = s1+1
        return res


a = Solution()
print(a.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
