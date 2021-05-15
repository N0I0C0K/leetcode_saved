from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        tar = [arr[0]]
        for i in range(1,len(arr)):
            tar.append(tar[i-1]^arr[i])
        res = []
        for a,b in queries:
            if a==b:
                res.append(arr[a])
            else:
                if a > 0:
                    res.append(tar[a-1]^tar[b])
                else:
                    res.append(tar[b])
        return res

a = Solution()
print(a.xorQueries([4,8,2,10],[[2,3],[1,3],[0,0],[0,3]]))