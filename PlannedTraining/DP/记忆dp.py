# https://www.luogu.com.cn/problem/P1048
# 22/3/21

def main():
    t, m = map(int, input().split())
    cost, mget = [0]*103, [0]*103

    for i in range(m):
        tc, gm = map(int, input().split())
        cost[i], mget[i] = tc, gm
    mem = [[-1 for i in range(1003)] for j in range(103)]

    def dfs(pos: int, tleft: int) -> int:
        if mem[pos][tleft] != -1:
            return mem[pos][tleft]
        if pos == m:
            mem[pos][tleft] = 0
            return 0
        dfs1 = dfs2 = -1e6
        dfs1 = dfs(pos+1, tleft)
        if tleft >= cost[pos]:
            dfs2 = dfs(pos+1, tleft-cost[pos])+mget[pos]
        mem[pos][tleft] = max(dfs1, dfs2)
        return mem[pos][tleft]
    print(dfs(0, t))


main()
