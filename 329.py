from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        def bfs     