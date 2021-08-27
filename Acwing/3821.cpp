#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
using ppair = pair<int, int>;
const int inf = 0x3f3f3f3f;

ppair times[500010];
int main()
{
    int t;
    scanf("%d",&t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d%d",&times[i].second,&times[i].first);
    }
    sort(times, times+t);
    int n = 1;
    int pidx = 0;
    int idx = 1;
    while (idx<t)
    {
        if(times[idx].second>times[pidx].first)
        {
            n++;
            pidx = idx;
        }
        idx++;
    }
    printf("%d",n);
    return 0;
}