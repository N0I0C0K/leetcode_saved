from typing import List

class Solution1:
    def canReach(self, arr: List[int], start: int) -> bool:
        rod = []
        rod.append(start)
        len_a = len(arr)
        is_vis = [False]*len_a
        while len(rod) > 0:
            idx = rod.pop(0)
            is_vis[idx] = True
            if arr[idx] == 0:
                return True
            if idx+arr[idx] < len_a and not is_vis[idx+arr[idx]]:
                rod.append(idx+arr[idx])
            if idx-arr[idx] >= 0 and not is_vis[idx-arr[idx]]:
                rod.append(idx-arr[idx])
        return False

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        

a = Solution()
print(a.canReach([4,2,3,0,3,1,2], 0))