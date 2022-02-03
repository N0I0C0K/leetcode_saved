#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;
const int maxn = 1e3 + 5;

int far[maxn]; //储存他是哪个集合的
int cnt;       //集合个数, 一开始等于n(n个独立集合)
//返回x节点的源节点
int find(int x)
{
    return far[x] == x ? x : (far[x] = find(far[x]));
}

//将两个节点化为一个集合
void unionn(int x, int y)
{
    int rx = find(x), ry = find(y);
    if (rx == ry)
        return;
    cnt--;
    far[rx] = ry;
}

struct edge
{
    int u, v, t;
} edges[100005];

bool cmp(edge l, edge r)
{
    return l.t <= r.t;
}

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    cnt = n;
    for (int i = 1; i <= n; ++i)
    {
        far[i] = i;
    }
    for (int i = 0; i < m; ++i)
    {
        scanf("%d%d%d", &edges[i].u, &edges[i].v, &edges[i].t);
    }
    sort(edges, edges + m, cmp);
    for (int i = 0; i < m; ++i)
    {
        unionn(edges[i].u, edges[i].v);
        if (cnt == 1)
        {
            printf("%d", edges[i].t);
            break;
        }
    }
    if (cnt > 1)
        printf("-1");
    return 0;
}