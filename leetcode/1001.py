from typing import *


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        points: Set[Tuple[int, int]] = set()
        row, col, din, rdin = Counter(), Counter(), Counter(), Counter()
        for r, c in lamps:
            if (r, c) in points:
                continue
            points.add((r, c))
            row[r] += 1
            col[c] += 1
            din[c-r] += 1
            rdin[c+r] += 1
        ans = [0] * len(queries)
        for i, (r, c) in enumerate(queries):
            if row[r] or col[c] or din[c-r] or rdin[c+r]:
                ans[i] = 1
            for x in range(r-1, r+2):
                for y in range(c-1, c+2):
                    if x < 0 or x >= n or y < 0 or y >= n or (x, y) not in points:
                        continue
                    points.remove((x, y))
                    row[x] -= 1
                    col[y] -= 1
                    din[y-x] -= 1
                    rdin[x+y] -= 1
        return ans
