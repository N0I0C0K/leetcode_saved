//https://ac.nowcoder.com/acm/problem/14694
#include<cstdio>
#include<cstring>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;
const int maxn = 4e5+10;
int nums[maxn];
int kmp[maxn];
int t,n,m,k;
int fkmp()
{
    int end = n+m-2,res = 0;
    memset(kmp, 0, sizeof kmp);
    for (int i = 1; i < end; ++i)
    {
        int j = kmp[i-1];
        while(j>0&&((nums[j]+nums[i])%k+k)%k != 0) j = kmp[j-1];
        if(((nums[j]+nums[i])%k+k)%k == 0) j++;
        kmp[i] = j;
    }
    for (int i = m+m-3; i < end; ++i)
    {
        if (kmp[i] == m-1)
        {
            res++;
        }
    }
    return res;
}

int main()
{
    scanf("%d",&t);
    while (t--)
    {
        int pre,now;
        scanf("%d%d%d",&n,&m,&k);
        for (int i = m; i < n+m; ++i)
        {
            scanf("%d",&now);
            if(i>m)
                nums[i-2] = now-pre;//((now-pre)%k+k)%k;
            pre = now;
            //scanf("%d",&nums[i]);
        }
        for (int i = 0; i < m; ++i)
        {
            scanf("%d",&now);
            if(i>0)
                nums[i-1] = now-pre;//((now-pre)%k+k)%k;
            pre = now;
            //scanf("%d",&nums[i]);
        }
        printf("%d\n",fkmp());
    }
    return 0;
}