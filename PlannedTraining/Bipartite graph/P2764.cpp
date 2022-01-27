//https://www.luogu.com.cn/problem/P2764
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 155;
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
    scanf("%d%d", &n, &m);
    int u = 0, v = 0;
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d", &u, &v);
        mmap[u][v] = true;
    }

    int ans = 0;
    for (int i = 1; i <= n; ++i)
    {
        memset(vis, false, sizeof vis);
        if (dfs(i))
            ans++;
    }

    return 0;
}