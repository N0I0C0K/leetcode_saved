#include<cstdio>
using ll = long long;
using namespace std;
const ll M = 998244353;
ll fast_pow(ll x,ll n,ll p)
 {
    ll temp;
    x=x%p;
    if(n==0)///终止条件
    {
        return 1;
    }
    temp=fast_pow((x*x)%p,n>>1,p);
    if(n&1)
    {
        temp =temp*x%p;///消除指数为奇数的影响
    }
    return temp%p;
 }

ll power(ll x, ll y, ll p)
{
    ll res = 1;      // Initialize result

    x = x % p;  // Update x if it is more than or 
                // equal to p

    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;

        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;  
    }
    return res;
}

ll mod(ll a,ll b)
{
    return (a%M)*(((b%M)+M)%M)%M;
}

int main()
{
    ll n,a,b,c;
    scanf("%lld",&n);
    while(n--)
    {
        scanf("%d%d%d",&a,&b,&c);
        if(c%2 == 0)
        {
            ll k = power(2,c/2, M);
            printf("%lld %lld\n",mod(k,a),mod(k,b));
        }
        else
        {
            ll k = power(2, (c-1)/2, M);
            printf("%lld %lld\n",mod(k,a+b), mod(k,a-b));
        }
    }
    return 0;
}