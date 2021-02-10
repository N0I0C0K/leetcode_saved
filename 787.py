from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(K+1):
            dist[src][i] = 0
        for flight in flights:
            if flight[0] == src:
                dist[flight[1]][0] = flight[2]
        for i in range(K+1):
            for flight in flights:
                begin = flight[0]
                end = flight[1]
                if dist[begin][i-1] != float('inf'):
                    dist[end][i] = min(dist[begin][i-1]+flight[2], dist[end][i])
        return -1 if dist[dst][K] == float('inf') else dist[dst][K]

a = Solution()
a.findCheapestPrice(3,
[[0,1,100],[1,2,100],[0,2,500]],
0,
2,
1)