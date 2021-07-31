#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>

const int MAX = 1000000;

int map[1010][1010];
int dist[1010];
int n,m;
using namespace std;

void min_len(int x)
{
    dist[x] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> que;
    que.emplace(0, x);
    while (!que.empty())
    {
        auto temp = que.top();
        que.pop();
        for (size_t i = 1; i <= n; i++)
        {
            if(map[temp.second][i] < MAX && dist[temp.second]+map[temp.second][i] < dist[i])
            {
                dist[i] = dist[temp.second]+map[temp.second][i];
                que.emplace(dist[i], i);
            }
        }   
    }
}

int main()
{
    int x,y,c;
    scanf("%d%d",&n,&m);
    memset(map, MAX, sizeof(map));
    memset(dist, MAX, sizeof(dist));
    for (size_t i = 0; i < m; ++i)
    {
        scanf("%d%d%d",&x,&y,&c);
        map[x][y] = c;
    }
    min_len(1);
    printf("%d", dist[n]);
    return 0;
}