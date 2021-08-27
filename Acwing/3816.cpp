#include<cstdio>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
using ll = long long;
using uint = unsigned int;
const int inf = 0x3f3f3f3f;

ll nums[100010];

int main()
{
    int t,n;
    ll temp,res;
    set<ll> keys;
    scanf("%d",&t);
    while (t--)
    {
        scanf("%d",&n);
        bool ok = false;
        res = 0;
        keys.clear();
        for (int i = 0; i < n; ++i)
        {
            scanf("%lld",&temp);
            res+=temp;
            nums[i] = temp;
        }
        temp = 0;
        for (int i = 0; i < n; ++i)
        {
            temp += nums[i];
            keys.insert(nums[i]);
            ll left = temp+temp;
            if(left > res)
            {
                if(((left-res)&1) == 0 && keys.count((left-res)/2))
                {
                    ok = true;
                    break;
                } 
            }
            else if(left == res)
            {
                ok = true;
                break;
            }
        }
        keys.clear();
        temp = 0;
        reverse(nums, nums+n);
        for (int i = 0; i < n; ++i)
        {
            temp += nums[i];
            keys.insert(nums[i]);
            if((temp+temp) > res)
            {
                if(((2*temp-res)&1) == 0 && keys.find((2*temp-res)/2) != keys.end())
                {
                    ok = true;
                    break;
                }   
            }
            else if((temp + temp) == res)
            {
                ok = true;
                break;
            }
        }
        
        if(ok)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}