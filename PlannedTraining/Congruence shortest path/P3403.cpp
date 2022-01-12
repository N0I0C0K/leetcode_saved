// https://www.luogu.com.cn/problem/P3403
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;
//类型, 如果需要long long就改
using stype = long long;

const int maxm = 100010 << 1; //边的最大数量;
const int maxn = 100010;      //节点的最大数量
int cnt = 0;
int p[maxn]; //节点指向的边

int n, m;           //n个节点 m条边
bool inqueue[maxn]; //是否在队列里
stype dis[maxn];    //距离
int in[maxn];       //进入队列的次数

struct
{
    stype w, to, next;
} edges[maxm]; //edge[0] is None, also we see if it's zero to judge it has been completed

void addEdge(stype from, stype to, stype weight)
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
    queue<stype> que;
    que.push(s);
    inqueue[s] = true;
    in[s]++;
    dis[s] = 1;
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
    ll h;
    scanf("%lld", &h);
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    n = a;
    if (a == 1 || b == 1 || c == 1)
    {
        printf("%lld\n", h);
        return 0;
    }
    for (int i = 0; i < a; ++i)
    {
        addEdge(i, (i + c) % a, c);
        addEdge(i, (i + b) % a, b);
    }
    spfa(0);
    ll ans = 0;
    for (int i = 0; i < a; ++i)
    {
        if (h >= dis[i])
            ans += (h - dis[i]) / a + 1;
    }
    printf("%lld\n", ans);
    return 0;
}