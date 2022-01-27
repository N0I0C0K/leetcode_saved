//https://www.luogu.com.cn/problem/P2756

#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 105;
int n, m;

bool mmap[maxn][maxn] = {false};
int match[maxn] = {0};
bool vis[maxn] = {false};

bool dfs(int u)
{
    for (int v = m + 1; v <= n; ++v)
    {
        if (mmap[u][v] && !vis[v])
        {
            vis[v] = true;
            if (!match[v] || dfs(match[v]))
            {
                match[v] = u;
                return true;
            }
        }
    }
    return false;
}

int main()
{
    scanf("%d%d", &m, &n);
    int u = 0, v = 0;
    scanf("%d%d", &u, &v);
    while (u != -1 && v != -1)
    {
        mmap[u][v] = true;
        scanf("%d%d", &u, &v);
    }
    int ans = 0;
    for (int i = 1; i <= m; ++i)
    {
        memset(vis, false, sizeof vis);
        if (dfs(i))
            ans++;
    }
    printf("%d\n", ans);
    for (int i = m + 1; i <= n; ++i)
    {
        if (match[i])
            printf("%d %d\n", match[i], i);
    }
    return 0;
}