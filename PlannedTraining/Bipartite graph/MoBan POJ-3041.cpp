// https://vjudge.net/problem/POJ-3041#author=HUO_ZHE
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int inf = 0x3f3f3f3f;

const int maxn = 505;
bool mmap[maxn][maxn] = {false};
bool vis[maxn] = {false};
int match[maxn] = {0};

int n, k;

bool path(int u)
{
    for (int v = 1; v <= n; ++v)
    {
        if (mmap[u][v] && !vis[v])
        {
            vis[v] = true;
            if (!match[v] || path(match[v]))
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
    scanf("%d%d", &n, &k);
    int u, v;
    for (int i = 0; i < k; i++)
    {
        scanf("%d%d", &u, &v);
        mmap[u][v] = true;
    }
    int res = 0;
    for (int i = 1; i <= n; ++i)
    {
        memset(vis, false, sizeof vis);
        if (path(i))
            ++res;
    }
    printf("%d\n", res);
    return 0;
}