// https://www.luogu.com.cn/problem/P2863
#include <stack>
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
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
int deep = 0;             //递归次数(不是深度)

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
    scanf("%d%d", &n, &m);
    int a, b;
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d", &a, &b);
        g[a].push_back(b);
    }
    for (int i = 1; i <= n; ++i)
    {
        if (!dfn[i])
            tarjan(i);
    }
    for (int i = 1; i <= n; ++i)
    {
        cnt[color[i]]++;
    }
    int ans = 0;
    for (int i = 1; i <= sum; ++i)
    {
        if (cnt[i] > 1)
        {
            ans++;
        }
    }
    printf("%d\n", ans);
    return 0;
}