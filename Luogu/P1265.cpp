//https://www.luogu.com.cn/problem/P1265
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
const int maxn = 5010;
const double INF = 1e9;

bool vis[maxn];
double w[maxn];
int b[maxn];

int map[maxn][2];

int n;

double dist(int i,int j)
{
    return sqrt(pow(map[i][0]-map[j][0], 2)+pow(map[i][1]-map[j][1], 2));
}

double prim()
{
    for(int i = 0;i<n;++i)
    {
        vis[i] = false;
        w[i] = dist(0,i);
        b[i] = 0;
    }
    vis[0] = true;
    int midx = 0;
    double mi = 0;
    double ans = 0;
    for(int i = 1;i<n;++i)
    {
        mi = INF;
        for(int j = 0;j<n;++j)
        {
            if(!vis[j] && w[j] < mi)
            {
                mi = w[j];
                midx = j;
            }
        }
        vis[midx] = true;
        ans+=mi;
        for(int j = 0;j<n;++j)
        {
            double a = dist(midx,j);
            if(!vis[j] && a<w[j])
                w[j] = a;
        }
    }
    return ans;
}

int main()
{
    scanf("%d",&n);
    for(int i = 0;i<n;++i)
    {
        scanf("%d%d",&map[i][0],&map[i][1]);
    }
    printf("%.2lf",prim());
    return 0;
}