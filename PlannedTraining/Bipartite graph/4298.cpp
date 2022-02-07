//https://www.acwing.com/problem/content/4301/

#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 105;
int n, m, k;
bool mmap[maxn][maxn] = {false}; //邻接矩阵
bool vis[maxn] = {false};
int match[maxn] = {0}; //储存B集合每个点连接的A

int man[maxn], woman[maxn];

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
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", man + i);
    }
    scanf("%d", &m);
    for (int i = 1; i <= m; i++)
    {
        scanf("%d", woman + i);
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; ++j)
        {
            if (abs(man[i] - woman[j]) <= 1)
                mmap[i][j] = true;
        }
    }
    int ans = 0; //最大匹配数
    for (int i = 1; i <= n; ++i)
    {
        memset(vis, false, sizeof vis);
        if (dfs(i))
            ++ans;
    }
    printf("%d", ans);
    return 0;
}