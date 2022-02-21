from typing import *
from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        que: Deque[int] = deque()
        time = [-1]*n
        force: List[list] = [[] for _ in range(n)]
        for i, f in enumerate(dominoes):
            if f != '.':
                que.append(i)
                time[i] = 0
                force[i].append(f)
        res = ['.']*n

        while que:
            i = que.popleft()
            if len(force[i]) == 1:

                res[i] = f = force[i][0]
                ni = i-1 if f == 'L' else i+1
                if 0 <= ni < n:

                    t = time[i]
                    if time[ni] == -1:
                        que.append(ni)
                        time[ni] = t+1
                        force[ni].append(f)
                    elif time[ni] == t+1:
                        force[ni].append(f)

        return ''.join(res)
