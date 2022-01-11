//https://www.luogu.com.cn/problem/P3275
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

const int maxm = 20; //边的最大数量;
const int maxn = 20; //节点的最大数量
int cnt = 0;
int p[maxn]; //节点指向的边

int n, m;           //n个节点 m条边
bool inqueue[maxn]; //是否在队列里
int dis[maxn];      //距离
int in[maxn];       //进入队列的次数

struct
{
    int w, to, next;
} edges[maxm]; //edge[0] is None, also we see if it's zero to judge it has been completed

void addEdge(int from, int to, int weight)
{
    edges[++cnt].to = to;
    edges[cnt].next = p[from];
    edges[cnt].w = weight;
    p[from] = cnt;
}

// 如果不存在环的 返回true, 否则返回false
// 求的是s 到每个节点的最短距离
bool spfa(int s)
{
    memset(dis, inf, sizeof dis);
    memset(inqueue, false, sizeof inqueue);
    memset(in, 0, sizeof in);
    queue<int> que;
    que.push(s);
    inqueue[s] = true;
    in[s]++;
    dis[s] = 0;
    while (!que.empty())
    {
        int t = que.front();
        que.pop();
        inqueue[t] = false;
        for (int i = p[t]; i; i = edges[i].next)
        {
            auto to = edges[i].to;
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

int main(int argc, char const *argv[])
{
    int x, a, b;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d%d", &x, &a, &b);
        if (x == 1)
        {
            addEdge(a, b, 0);
            addEdge(b, a, 0);
        }
        else if (x == 2)
        {
            addEdge(b, a, 1);
        }
        else if (x == 3)
        {
            addEdge(a, b, 0);
        }
        else if (x == 4)
        {
            addEdge(a, b, 1);
        }
        else
        {
            addEdge(b, a, 0);
        }
    }
    for (int i = 1; i <= n; ++i)
        addEdge(0, i, 0);
    if (spfa(0))
    {
        ll res = 0;
        for (int i = 1; i <= n; ++i)
        {
            res += dis[i];
        }
        printf("%lld\n", res);
    }
    return 0;
}
