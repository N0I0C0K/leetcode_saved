//小雨坐地铁 https://ac.nowcoder.com/acm/problem/26257
// 得用分层图
#include<cstdio>
//#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
using namespace std;
using ppair = pair<int, int>;
const int INF = 0x3f3f3f3f;
const int MAXN = 1e7;
int map[1010][1010];

int e[MAXN],ne[MAXN],w[MAXN],h[MAXN],idx = 0;

int dist[MAXN];
bool vis[MAXN];
int n,m,s,t;

void add(int a,int b,int c)
{
    e[idx] = b;
    ne[idx] = h[a];
    w[idx] = c;
    h[a] = idx++;
}


void dijistra(int x)
{
    memset(dist, INF, sizeof(dist));
    memset(vis, false, sizeof vis);
    dist[x] = 0;
    priority_queue<ppair, vector<ppair>, greater<ppair>> que;
    que.emplace(0,x);
    while(!que.empty())
    {
        auto t = que.top();
        que.pop();
        if(vis[t.second])
            continue;
        vis[t.second] = true;
        for(int i = h[t.second];i != -1;i = ne[i])
        {
            if(dist[e[i]] > dist[t.second]+w[i])
            {
                dist[e[i]] = dist[t.second]+w[i];
                que.emplace(dist[e[i]],e[i]);
            }
        }
    }
}

int main()
{
    scanf("%d%d%d%d",&n,&m,&s,&t);
    //memset(map, INF, sizeof(map));
    memset(h, -1, sizeof h);
    int a,b,c,x,pre;
    for (size_t i = 1; i <= m; i++)
    {
        scanf("%d%d%d",&a,&b,&c);
        pre = 0;
        for (size_t j = 0; j < c; ++j)
        {
            scanf("%d",&x);
            add((i-1)*n+x, n*m+x, 0);
            add(n*m+x, (i-1)*n+x, a);
            if(j != 0)
            {
                add((i-1)*n+pre, (i-1)*n+x, b);
                add((i-1)*n+x, (i-1)*n+pre, b);
            }
            pre = x;
        }
    }
    dijistra(n*m+s);
    if(dist[n*m+t] != INF)  printf("%d",dist[n*m+t]);
    else printf("-1");
    return 0;
}