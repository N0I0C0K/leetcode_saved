#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
using ppair = pair<int, int>;
ppair rings[1010];

int main()
{
    int n,a,b,x,y;
    scanf("%d",&n);
    for(int tt = 0;tt<n;++tt)
    {
        scanf("%d%d",&a,&b);
        for(int ttt = 0;ttt < b;++ttt)
        {
            scanf("%d%d",&rings[ttt].first, &rings[ttt].second);
        }
        sort(rings, rings+b);
        printf("%d\n", b);
        for(int i = 0;i<b;++i)
        {
            if(i == 0)
                printf("%d %d\n",rings[i].first, rings[b-1].second);
            else
                printf("%d %d\n",rings[i].first, rings[i-1].second);
        }
    }
    return 0;
}