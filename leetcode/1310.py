from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        tar = [arr[0]]
        for i in range(1,len(arr)):
            tar.append(tar[i-1]^arr[i])
        res = []
        for a,b in queries:
            res.append(tar[b]^tar[a])
        return res

a = Solution()
print(a.xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))