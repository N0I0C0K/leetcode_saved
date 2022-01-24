#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 505;
int n, m, k;
bool mmap[maxn][maxn] = {false};
bool vis[maxn] = {false};
int match[maxn] = {0};

bool dfs(int u)
{
    for (int v = 1; v <= m; ++v)
    {
        if (!vis[v] && mmap[u][v])
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
    scanf("%d%d%d", &n, &m, &k);
    int u, v;
    for (int i = 0; i < k; ++i)
    {
        scanf("%d%d", &u, &v);
        mmap[u][v] = true;
    }
    int ans = 0;
    for (int i = 1; i <= n; ++i)
    {
        memset(vis, false, sizeof vis);
        if (dfs(i))
            ++ans;
    }
    printf("%d", ans);
    return 0;
}