#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 5e5 + 5;
const int maxm = maxn << 1; //边的最大数量;
int cnt = 0;
int p[maxn] = {0}; //节点指向的边, 这里为了简单用了同一个maxn

bool vis[maxn] = {false};
int first[maxn] = {};
int deepth[maxm] = {};
int ver[maxm] = {};

int lg[maxm] = {-1};     //预处理log_2_(x)
int mmin[maxm][50] = {}; //表示mmax[i][j]表示 a[i][i+2^j-1]区间内的最大值

int tol = 0;

struct
{
    int to, next;
} edges[maxm]; // edge[0] is None, also we see if it's zero to judge it has been completed

void addEdge(int from, int to)
{
    edges[++cnt].to = to;
    edges[cnt].next = p[from];
    p[from] = cnt;
}

void dfs(int u, int deep = 1)
{
    vis[u] = true;
    ver[++tol] = u;
    deepth[tol] = deep;
    first[u] = tol;
    for (int v = p[u]; v; v = edges[v].next)
    {
        int to = edges[v].to;
        if (!vis[to])
        {
            dfs(to, deep + 1);
            ver[++tol] = u;
            deepth[tol] = deep;
        }
    }
}

void initST()
{
    for (int i = 1; i <= tol; ++i)
    {
        lg[i] = lg[i >> 1] + 1;
        mmin[i][0] = i;
    }
    int a, b;
    for (int i = 1; i <= lg[tol]; ++i)
    {
        for (int j = 1; j + (1 << i) - 1 <= tol; ++j)
        {
            a = mmin[j][i - 1], b = mmin[j + (1 << (i - 1))][i - 1];
            if (deepth[a] < deepth[b])
                mmin[j][i] = a;
            else
                mmin[j][i] = b;
        }
    }
}

int rmq(int l, int r)
{
    int len = lg[r - l + 1];
    int a = mmin[l][len], b = mmin[r - (1 << len) + 1][len];
    return deepth[a] < deepth[b] ? a : b;
}

int lca(int a, int b)
{
    int x = first[a], y = first[b];
    if (x > y)
        swap(x, y);
    return ver[rmq(x, y)];
}

int main()
{
    int n, m, s;
    scanf("%d%d%d", &n, &m, &s);
    int u, v;
    for (int i = 1; i < n; ++i)
    {
        scanf("%d%d", &u, &v);
        addEdge(u, v);
        addEdge(v, u);
    }
    dfs(s);
    initST();
    while (m--)
    {
        scanf("%d%d", &u, &v);
        printf("%d\n", lca(u, v));
    }

    return 0;
}