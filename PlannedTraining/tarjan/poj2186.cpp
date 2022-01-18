#include <stack>
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int inf = 0x3f3f3f3f;

const int maxn = 10010; //点的数量
int n, m;
vector<int> g[maxn];      //邻接表储存图
stack<int> res;           //保存连通分量的中间变量
int color[maxn] = {0};    //标记, 具有相同标记的是一组强连通分量
int dfn[maxn] = {0};      //代表n被搜索到的时候的深度
int low[maxn] = {0};      //整个连通分量的最小深度
bool vis[maxn] = {false}; //是否在res里面
int cnt[maxn] = {0};      // 储存强连通分量的个数
int sum = 0;              //强连通分量的个数
int deep = 0;

int du[maxn] = {0};

void init()
{
    memset(color, 0, sizeof color);
    memset(dfn, 0, sizeof dfn);
    memset(low, 0, sizeof low);
    memset(vis, 0, sizeof vis);
    memset(cnt, 0, sizeof cnt);
    memset(du, 0, sizeof du);
    deep = 0;
    sum = 0;
    while (!res.empty())
    {
        res.pop();
    }
    for (int i = 1; i <= n; i++)
    {
        g[i].clear();
    }
}

void tarjan(int u)
{
    dfn[u] = ++deep;
    low[u] = deep;
    vis[u] = true;
    res.push(u);
    int l = g[u].size();
    for (int i = 0; i < l; ++i)
    {
        int v = g[u][i];
        if (!dfn[v])
        {
            tarjan(v);
            low[u] = min(low[u], low[v]);
        }
        else
        {
            if (vis[v])
                low[u] = min(low[u], low[v]);
        }
    }
    if (dfn[u] == low[u])
    {
        color[u] = ++sum;
        vis[u] = false;
        while (res.top() != u)
        {
            color[res.top()] = sum;
            vis[res.top()] = false;
            res.pop();
        }
        res.pop();
    }
}

int main()
{

    while (scanf("%d%d", &n, &m) != EOF)
    {
        init();
        int u, v;
        for (int i = 0; i < m; ++i)
        {
            scanf("%d%d", &u, &v);
            g[u].push_back(v);
        }
        for (int i = 1; i <= n; ++i)
        {
            if (!dfn[i])
                tarjan(i);
        }

        for (int i = 1; i <= n; ++i)
        {
            /******  The different   ********/
            int l = g[i].size();
            for (int j = 0; j < l; ++j)
            {
                int v = g[i][j];
                if (color[i] != color[v])
                {
                    du[color[i]]++;
                }
            }
            /*******************************/
            cnt[color[i]]++;
        }
        int tmp = 0, ans = 0;
        for (int i = 1; i <= sum; ++i)
        {
            if (du[i] == 0)
            {
                tmp++;
                ans = cnt[i];
            }
        }
        if (tmp != 1)
        {
            printf("0\n");
        }
        else
        {
            printf("%d\n", ans);
        }
    }
    return 0;
}