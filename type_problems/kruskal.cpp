//https://ac.nowcoder.com/acm/problem/15108 最小生成树练习
#include<cstdio>
#include<algorithm>

using namespace std;

const int maxn = 1e5+10;

struct Node
{
    int from,to,dis;
}edge[maxn];
int far[150];   //并采集
int c,n,m;

bool cmp(Node a,Node b)
{
    return a.dis<b.dis;
}

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
    int k = 0;
    int total = 0;
    scanf("%d%d%d",&c,&n,&m);
    for(int t = 0;t<n;++t)
    {
        scanf("%d%d%d",&edge[t].from,&edge[t].to,&edge[t].dis);
    }
    for(int i = 0;i<=m;++i) far[i] = i;
    sort(edge,edge+n,cmp);
    for(int i = 0;i<n;++i)
    {
        if(k+1 == m-1)
            break;
        if(find(edge[i].from) != find(edge[i].to))
        {
            unionn(edge[i].from, edge[i].to);
            total+=edge[i].dis;
            k++;
        }
    }
    if(total<=c)
        printf("Yes");
    else
        printf("No");
    return 0;
}