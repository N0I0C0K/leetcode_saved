//小雨坐地铁 https://ac.nowcoder.com/acm/problem/26257
#include<cstdio>
//#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
using namespace std;
using ppair = pair<int, int>;
const int INF = 0x3f3f3f3f;
int map[1010][1010];
int dist[1010];
int n,m,s,t;

void dijistra(int x)
{
    memset(dist, INF, sizeof(dist));
    dist[x] = 0;
    priority_queue<ppair, vector<ppair>, greater<ppair>> que;
    que.emplace(0,x);
    while(!que.empty())
    {
        auto t = que.top();
        que.pop();
        for(int i = 1;i <= n;++i)
        {
            if(map[t.second][i] < INF && dist[t.second]+map[t.second][i] < dist[i])
            {
                dist[i] = dist[t.second]+map[t.second][i];
                que.emplace(dist[i],i);
            }
        }
    }
}

int main()
{
    scanf("%d%d%d%d",&n,&m,&s,&t);
    memset(map, INF, sizeof(map));
    int a,b,c;
    for (size_t i = 0; i < m; i++)
    {
        scanf("%d%d%d",&a,&b,&c);
        for (size_t j = 0; j < c; ++j)
        {
            scanf("%d",&dist[j]);
        }
        for (int j = 0; j < c; ++j)
        {
            for (int k = 0; k < c; ++k)
            {
                map[dist[j]][dist[k]] = a+abs(k-j)*b;
            }
        }
    }
    dijistra(s);
    if(dist[t] != INF)  printf("%d",dist[t]);
    else printf("-1");
    return 0;
}