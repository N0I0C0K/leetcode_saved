from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        len_e = len(edges)
        tar = [i for i in range(len_e+1)]
        def find_parent(a:int):
            if tar[a] == a:
                return a
            return find_parent(tar[a])
        for i in edges:
            if find_parent(i[0]) == find_parent(i[1]):
                return i
            tar[find_parent(i[1])] = find_parent(i[0])