//https://www.luogu.com.cn/problem/P5960

#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxn = 5005;

int cnt = 0;
int p[maxn];

int n, m;
bool inqueue[maxn];
int dis[maxn];
int in[maxn];

struct
{
    int to, w, next;
} edges[maxn];

void addEdge(int from, int to, int weight)
{
    edges[++cnt].to = to;
    edges[cnt].next = p[from];
    edges[cnt].w = weight;
    p[from] = cnt;
}

bool spfa(int s)
{
    memset(dis, inf, sizeof dis);
    memset(in, 0, sizeof in);
    memset(inqueue, false, sizeof inqueue);
    dis[s] = 0;
    queue<int> que;
    // for (int i = 1; i <= n; ++i)
    // {
    //     que.push(i);
    //     inqueue[i] = true;
    //     in[i]++;
    // }
    que.push(s);
    inqueue[s] = true;
    in[s]++;
    while (!que.empty())
    {
        int t = que.front();
        que.pop();
        inqueue[t] = false;
        for (int i = p[t]; i; i = edges[i].next)
        {
            int to = edges[i].to;
            if (dis[to] > dis[t] + edges[i].w)
            {
                dis[to] = dis[t] + edges[i].w;
                if (!inqueue[to])
                {
                    que.push(to);
                    inqueue[to] = true;
                    if (++in[to] > n)
                        return false;
                }
            }
        }
    }
    return true;
}

int main()
{
    int a, b, c;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d%d", &a, &b, &c);
        addEdge(b, a, c);
    }
    for (int i = 0; i <= n; ++i)
        addEdge(n + 1, i, 0);
    if (spfa(n + 1))
    {
        for (int i = 1; i <= n; ++i)
            printf("%d%c", dis[i], i < n ? ' ' : '\n');
    }
    else
        printf("NO\n");
    return 0;
}