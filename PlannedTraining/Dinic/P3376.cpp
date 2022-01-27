#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 205;
const int maxm = 5005 << 1;
int s, t; //源点, 汇点
int n, m;
int depth[maxn];
int cur[maxn];

int cnt = -1;   //边从0开始
int head[maxn]; //节点指向的边, 这里为了简单用了同一个maxn
struct Edge
{
    int w, to, next = -1;
} edges[maxm]; //edge[0] is None, also we see if it's zero to judge it has been completed

void _addEdge(int from, int to, int weight)
{
    edges[++cnt].to = to;
    edges[cnt].next = head[from];
    edges[cnt].w = weight;
    head[from] = cnt;
}

void addEdge(int from, int to, int weight)
{
    _addEdge(from, to, weight);
    _addEdge(to, from, 0);
}

void init()
{
    memset(head, -1, sizeof head);
}

int dfs(int u, int dist)
{
    if (u == t)
        return dist;
    for (int &i = cur[u]; i != -1; i = edges[i].next)
    {
        Edge &edge = edges[i];
        if ((depth[edge.to] == depth[u] + 1) && edge.w)
        {
            int di = dfs(edge.to, min(dist, edge.w));
            if (di > 0)
            {
                edge.w -= di;
                edges[i ^ 1].w += di;
                return di;
            }
        }
    }
    return 0;
}

bool bfs()
{
    queue<int> que;
    while (!que.empty())
        que.pop();
    memset(depth, 0, sizeof depth);
    depth[s] = 1;
    que.push(s);
    do
    {
        int u = que.front();
        que.pop();
        for (int i = head[u]; i != -1; i = edges[i].next)
        {
            if ((edges[i].w > 0) && depth[edges[i].to] == 0)
            {
                depth[edges[i].to] = depth[u] + 1;
                que.push(edges[i].to);
            }
        }
    } while (!que.empty());
    if (depth[t] != 0)
        return true;
    return false;
}

ll dinic()
{
    ll ans = 0;
    while (bfs())
    {
        for (int i = 1; i <= n; ++i)
            cur[i] = head[i];
        while (int d = dfs(s, inf))
        {
            ans += d;
        }
    }
    return ans;
}

int main()
{
    init();
    scanf("%d%d%d%d", &n, &m, &s, &t);
    int u, v, w;
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d%d", &u, &v, &w);
        addEdge(u, v, w);
    }
    printf("%lld", dinic());
    return 0;
}