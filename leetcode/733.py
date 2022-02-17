from typing import *
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        que: Deque[Tuple[int, int]] = deque()
        n, m = len(image), len(image[0])
        vis = [[False for _ in image[0]] for k in image]
        que.append((sr, sc))
        tar = image[sr][sc]
        while len(que) > 0:
            x, y = que.popleft()
            if x < 0 or x >= n or y < 0 or y >= m or vis[x][y]:
                continue
            vis[x][y] = True
            t = image[x][y]
            if t != tar:
                continue
            image[x][y] = newColor
            for item in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                que.append(item)
        return image
