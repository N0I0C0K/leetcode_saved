from collections import deque


def main():
    tn = int(input())
    for _ in range(tn):
        n, k = map(int, input().split())
        vis = [0]*n
        q = deque()
        for i in map(int, input().split()):
            q.append(i-1)
        ans = 0
        while q:
            for _i in range(len(q)):
                t = q.popleft()
                vis[t] = 1
                for j in (t+1, t-1):
                    if 0 <= j < n and vis[j] == 0:
                        q.append(j)
            ans += 1
            if sum(vis) == n:
                break
        print(ans)


main()
