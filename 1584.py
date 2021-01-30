from typing import List
class Solution: #kruskal
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        len_p = len(points)
        res = list(range(len_p))
        dis = []
        rank = [1]*len_p

        def find(x:int):
            if res[x] == x:
                return x
            res[x] = find(res[x])
            return res[x]
        
        def union(x, y)->bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            if rank[fx] < rank[fy]:
                fx, fy = fy, fx
            rank[fx] += rank[fy]
            res[fy] = fx
            return True
        
        for i in range(len_p):
            for j in range(i+1, len_p):
                dis.append((dist(i, j), i, j))
        
        dis.sort()
        ret, nums = 0, 1
        for length, x, y in dis:
            if union(x,y):
                ret += length
                nums+=1
                if nums == len_p:
                    break
        return ret

class Solution1: #Prim
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        max_dis = 4000000
        len_p = len(points)
        v = list(range(len_p))
        vnem = []
        is_f = [False]*len_p
        lowcost = [max_dis]*len_p
        dis = []
        for i in range(len_p):
            temp = []
            for j in range(len_p):
                temp.append(dist(i,j))
            dis.append(temp)
        start = 0
        is_f[start] = True
#摸鱼😁😁😁,希望你可以找到这