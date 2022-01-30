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
bool vis[maxn] = {false};
int ans = 0;

void dfs(int u = 1)
{
    if (vis[u])
    {
        ++ans;
        return;
    }
    vis[u] = true;
    for (int i = 1; i <= n; ++i)
    {
        if (mmap[u][i])
            dfs(i);
    }
}

int main()
{
    scanf("%d%d", &n, &m);
    int u, v;
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d", &u, &v);
        mmap[u][v] = true;
        mmap[v][u] = true;
    }
    dfs();
    ans -= n;
    if (ans == 1)
        printf("YES");
    else
        printf("NO");
    return 0;
}