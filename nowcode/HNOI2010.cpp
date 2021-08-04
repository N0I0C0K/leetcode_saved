#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn = 5e4+5;

struct Node
{
    int from,to,dis;
    bool operator<(const Node a) const
    {
        return dis<a.dis;
    }
}edge[maxn];

int n,m,q;
int far[maxn];

int find(int x)
{
    if(far[x] == x)
        return x;
    return find(far[x]);
}

void unionn(int x,int y)
{
    far[find(y)] = find(x);
}

int main()
{
    scanf("%d%d%d",&n,&m,&q);
    for(int i = 0;i<m;++i)
    {
        scanf("%d%d%d", &edge[i].from, &edge[i].to, &edge[i].dis);
    }
    for(int i = 0;i<n;++i)
        far[i] = i;
    sort(edge, edge+m);
    int k = 0,ans = 0,maxx = 0,kk,tt;
    for(int i = 0;i<n;++i)
    {
        if(k+1 == n)
            break;
        if(find(edge[i].from) != find(edge[i].to))
        {
            unionn(edge[i].from, edge[i].to);
            ans+=edge[i].dis;
            k++;
            if(maxx<edge[i].dis)
                maxx = edge[i].dis;
        }
    }
    for(int i = 0;i<q;++i)
    {
        scanf("%d%d",&kk,&tt);
        printf("%d\n",ans+tt-maxx);
    }
    return 0;
}