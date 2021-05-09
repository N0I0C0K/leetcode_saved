from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        len_c = len(isConnected)
        con = [i for i in range(len_c)]
        
        def getParent(a:int):
            if con[a] == a:
                return a
            return getParent(con[a])

        for i in range(len_c):
            for j in range(0, i):
                if isConnected[j][i] == 1:
                    con[getParent(j)] = getParent(i)

        nums = 0
        for i in range(len_c):
            if i == con[i]:
                nums+=1
        return nums