#include<cstdio>
#include<cmath>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

int main()
{
    ll t,x,l,r,mid,row,c;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&x);
        l = 1,r = 1e5;
        while (l<=r)
        {
            mid = l+r>>1;
            if(mid*mid >= x)
                r = mid-1;
            else
                l = mid+1;
        }
        mid = l;
        ll al = mid*mid;
        if(al - x >= mid)
        {
            row = mid-(al-mid-x+1);
            c = mid;
        }
        else
        {
            c = al-x+1;
            row = mid;
        }
        printf("%lld %lld\n",row,c);
    }
    return 0;
}