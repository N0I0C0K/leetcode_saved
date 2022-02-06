from typing import *


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0]*(l := len(nums))
        mlist, elist, alist = [], [], []
        for i in nums:
            if i < pivot:
                mlist.append(i)
            elif i > pivot:
                alist.append(i)
            else:
                elist.append(i)
        return mlist+elist+alist
