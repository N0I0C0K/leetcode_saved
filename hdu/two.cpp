#include<cstdio>
#include<algorithm>
using namespace std;
using ll = long long;
ll nums[100010];

int main()
{
    ll n,a,b,l,r,x,t;
    scanf("%lld",&n);
    while(n--)
    {
        l = 1e9,r = 0,t=0;
        scanf("%lld%lld",&a,&b);
        if(a == 1)
        {
            printf("0\n");
            continue;
        }
        for(int i = 0;i<a;++i)  scanf("%d",&nums[i]);
        sort(nums,nums+a);
        for(int i = 0;i<a;++i)
        {
            x = nums[i];
            if(i>0)
            {
                if(x-b>r)
                {
                    t+=x-b-r-1;
                }
                else if(x+b<l)
                {
                    t+=l-x-b-1;
                }

            }
            l = min(l, x-b);
            r = max(r, x+b);
        }
        t = min(a,r-l-t+1);
        t = t==1?0:t;
        printf("%lld\n",t);
    }
    return 0;
}